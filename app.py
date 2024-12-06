# app.py

import streamlit as st
from simulation.model import UserModel, Change  # Now imports Change correctly
from ui.components import render_sidebar, display_simulation_results

import random
import pandas as pd  # Ensure pandas is imported

# Set the page configuration
st.set_page_config(
    page_title="User Satisfaction and NPS Simulation",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("User Satisfaction and NPS Simulation")

# Render Sidebar and get user inputs
user_inputs = render_sidebar()

# Unpack user inputs
num_users = user_inputs["num_users"]
num_steps = user_inputs["num_steps"]
csat_score = user_inputs["csat_score"]
initial_satisfaction = user_inputs["initial_satisfaction"]
random_seed = user_inputs["random_seed"]
run_simulation = user_inputs["run_simulation"]

if run_simulation:
    with st.spinner("Running simulation..."):
        # Set random seed for reproducibility
        random.seed(random_seed)

        # Initialize the Change object with CSAT score
        change = Change(csat_score=csat_score)
        
        # Initialize the model with updated initial satisfaction
        model = UserModel(num_users, change, initial_satisfaction)

        # Run the simulation
        for _ in range(num_steps):
            model.step()

        # Retrieve data
        model_data = model.datacollector.get_model_vars_dataframe()
        agent_data = model.datacollector.get_agent_vars_dataframe()
        comments = model.comments  # Now, comments should exist

        # Convert comments to DataFrame
        if comments:
            comments_df = pd.DataFrame(comments)
        else:
            comments_df = pd.DataFrame(columns=["agent_id", "group", "persona", "comment", "sentiment"])

    # Display Simulation Results using the UI module
    display_simulation_results(model, model_data, agent_data, comments_df)