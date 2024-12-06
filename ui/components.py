# ui/components.py

import streamlit as st
import pandas as pd
import io  # Essential for handling in-memory byte streams
from visualization.plots import (
    plot_comment_sentiment,
    plot_nps_by_persona,
    plot_aggregated_nps_over_time,
    plot_final_aggregated_nps,
    plot_group_nps
)
from simulation.personas import PERSONAS

def get_group_for_persona(persona_name):
    """
    Returns the group name for a given persona.

    Args:
        persona_name (str): The name of the persona.

    Returns:
        str: The group name to which the persona belongs.
    """
    for group, details in PERSONAS.items():
        for persona in details["personas"]:
            if persona["name"] == persona_name:
                return group
    return "Unknown"

def render_sidebar():
    """
    Renders the sidebar with all user input controls.

    Returns:
        dict: A dictionary containing all user inputs.
    """
    st.sidebar.header("Simulation Parameters")

    # Input controls
    num_users = st.sidebar.number_input(
        "Number of Users",
        min_value=100,
        max_value=10000,
        value=1000,
        step=100
    )
    num_steps = st.sidebar.number_input(
        "Number of Simulation Steps",
        min_value=1,
        max_value=100,
        value=50,
        step=1
    )
    csat_score = st.sidebar.slider(
        "CSAT Score",
        min_value=0.0,
        max_value=1.0,
        value=0.8,
        step=0.05
    )

    # Persona-specific initial satisfaction controls
    st.sidebar.header("Persona Initial Satisfaction")

    # Iterate through groups and personas to create sliders or inputs
    initial_satisfaction = {}
    for group, details in PERSONAS.items():
        st.sidebar.subheader(f"{group} Personas")
        for persona in details["personas"]:
            key = f"{group}_{persona['name']}_satisfaction"
            initial_satisfaction[persona["name"]] = st.sidebar.slider(
                f"{persona['name']} Initial Satisfaction",
                0,
                10,
                persona["attributes"].get("satisfaction", 5)
            )

    # Optional: Random Seed for reproducibility
    st.sidebar.header("Randomness Control")
    random_seed = st.sidebar.number_input(
        "Random Seed",
        value=42,
        step=1
    )

    # Run Simulation Button
    run_simulation = st.sidebar.button("Run Simulation")

    return {
        "num_users": num_users,
        "num_steps": num_steps,
        "csat_score": csat_score,
        "initial_satisfaction": initial_satisfaction,
        "random_seed": random_seed,
        "run_simulation": run_simulation
    }

def display_simulation_results(model, model_data, agent_data, comments_df):
    """
    Displays the simulation results in a structured layout.

    Args:
        model (UserModel): The simulation model instance.
        model_data (pd.DataFrame): Data collected from the model.
        agent_data (pd.DataFrame): Data collected from the agents.
        comments_df (pd.DataFrame): DataFrame of comments.
    """
    st.success("Simulation completed!")

    # Layout for the visualizations
    st.header("Simulation Results")

    # **1. Display Final Aggregated NPS as a Prominent Text at the Top**
    if not model_data.empty:
        final_nps = model_data['Overall NPS'].iloc[-1]
        st.markdown(f"### Final Aggregated NPS: **{final_nps:.2f}%**")
    else:
        st.markdown("### Final Aggregated NPS: **N/A**")

    # **2. Top Row: Final Aggregated NPS Plot and NPS Scores by Persona**
    col1, col2 = st.columns(2)

    with col1:
        # Plot Final Aggregated NPS
        if not model_data.empty:
            final_promoters = model_data['Promoters %'].iloc[-1]
            final_passives = model_data['Passives %'].iloc[-1]
            final_detractors = model_data['Detractors %'].iloc[-1]
            fig_final_nps = plot_final_aggregated_nps(final_promoters, final_passives, final_detractors)
            st.pyplot(fig_final_nps)
        else:
            st.write("No NPS data available to plot the final aggregated NPS.")

    with col2:
        # Plot NPS Scores by Persona
        if not agent_data.empty:
            # Extract the final step data
            if 'Step' in agent_data.index.names:
                final_step = agent_data.index.get_level_values('Step').max()
                final_agent_data = agent_data.xs(final_step, level='Step')
            else:
                final_agent_data = agent_data[agent_data['Step'] == agent_data['Step'].max()]

            # Calculate NPS per Persona
            nps_per_persona = []
            if not final_agent_data.empty and 'Persona' in final_agent_data.columns and 'NPS Rating' in final_agent_data.columns:
                for persona in final_agent_data['Persona'].unique():
                    persona_data = final_agent_data[final_agent_data['Persona'] == persona]
                    total = len(persona_data)
                    promoters = len(persona_data[persona_data['NPS Rating'] >= 9])
                    detractors = len(persona_data[persona_data['NPS Rating'] <= 6])
                    passives = total - promoters - detractors
                    nps_score = ((promoters - detractors) / total) * 100 if total > 0 else 0
                    group = get_group_for_persona(persona)
                    nps_per_persona.append({
                        'Group': group,
                        'Persona': persona,
                        'Promoters %': (promoters / total) * 100 if total > 0 else 0,
                        'Passives %': (passives / total) * 100 if total > 0 else 0,
                        'Detractors %': (detractors / total) * 100 if total > 0 else 0,
                        'NPS Score': nps_score
                    })
                nps_df = pd.DataFrame(nps_per_persona)

                if not nps_df.empty:
                    fig_nps_persona = plot_nps_by_persona(nps_df)
                    st.pyplot(fig_nps_persona)

                    # Display NPS per Persona Data
                    st.header("NPS Scores by Persona")
                    st.dataframe(nps_df[['Group', 'Persona', 'NPS Score']])
        else:
            st.write("No agent data available to plot NPS Scores by Persona.")

    # **3. Second Row: Comment Sentiment Counts and Aggregated NPS Over Time**
    col3, col4 = st.columns(2)

    with col3:
        # Plot Comment Sentiment Counts
        st.header("Comment Sentiment Counts")
        if not comments_df.empty:
            sentiment_counts = comments_df['sentiment'].value_counts()
            fig_sentiment = plot_comment_sentiment(sentiment_counts)
            st.pyplot(fig_sentiment)
        else:
            st.write("No comments to display.")

    with col4:
        # Plot Aggregated NPS Over Time
        st.header("Aggregated NPS Over Time")
        if not model_data.empty:
            fig_nps_time = plot_aggregated_nps_over_time(model_data)
            st.pyplot(fig_nps_time)
        else:
            st.write("No data available to plot the aggregated NPS.")

    # **4. Additional Visualization: Group-Level NPS**
    if 'Group NPS' in model_data.columns:
        group_nps = model_data['Group NPS'].iloc[-1]  # Assuming it's a dict
        st.header("NPS Scores by Group")
        df_group_nps = pd.DataFrame(list(group_nps.items()), columns=['Group', 'NPS Score'])
        st.dataframe(df_group_nps)
        fig_group_nps = plot_group_nps(group_nps)
        st.pyplot(fig_group_nps)

    # **5. Download Buttons**
    st.header("Download Simulation Results")

    # Download NPS by Persona as CSV
    if 'nps_df' in locals() and not nps_df.empty:
        csv_nps = nps_df[['Group', 'Persona', 'Promoters %', 'Passives %', 'Detractors %', 'NPS Score']].to_csv(index=False)
        st.download_button(
            label="Download NPS by Persona as CSV",
            data=csv_nps,
            file_name='nps_by_persona.csv',
            mime='text/csv',
        )

    # Download Group NPS as CSV
    if 'group_nps' in locals() and isinstance(group_nps, dict):
        df_group_nps = pd.DataFrame(list(group_nps.items()), columns=['Group', 'NPS Score'])
        csv_group_nps = df_group_nps.to_csv(index=False)
        st.download_button(
            label="Download Group NPS as CSV",
            data=csv_group_nps,
            file_name='group_nps.csv',
            mime='text/csv',
        )

    # Download Final NPS Plot as PNG
    if 'final_nps' in locals() and not model_data.empty:
        fig_final_nps_png = plot_final_aggregated_nps(final_promoters, final_passives, final_detractors)
        buf = io.BytesIO()
        fig_final_nps_png.savefig(buf, format='png')
        buf.seek(0)
        st.download_button(
            label="Download Final NPS Plot",
            data=buf,
            file_name="final_nps_plot.png",
            mime="image/png",
        )