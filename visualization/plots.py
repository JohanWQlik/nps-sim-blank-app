# visualization/plots.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_comment_sentiment(sentiment_counts):
    """
    Generates a bar chart for comment sentiment counts.

    Parameters:
    - sentiment_counts (pd.Series): Series with sentiment categories as index and counts as values.

    Returns:
    - fig (matplotlib.figure.Figure): The generated matplotlib figure.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='coolwarm', ax=ax)
    ax.set_title("Comment Sentiment Counts")
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Count")
    plt.tight_layout()
    return fig

def plot_nps_by_persona(nps_df):
    """
    Generates a bar chart for NPS scores by persona across groups.

    Parameters:
    - nps_df (pd.DataFrame): DataFrame with 'Group', 'Persona', and 'NPS Score' columns.

    Returns:
    - fig (matplotlib.figure.Figure): The generated matplotlib figure.
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(data=nps_df, x='Persona', y='NPS Score', hue='Group', palette='Set2', ax=ax)
    ax.axhline(0, color='gray', linestyle='--')
    ax.set_ylim(-100, 100)
    ax.set_title("NPS Score by Persona Across Groups")
    ax.set_xlabel("Persona")
    ax.set_ylabel("NPS Score (%)")
    ax.legend(title='Group', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    return fig

def plot_group_nps(group_nps):
    """
    Generates a bar chart for NPS scores by group.

    Parameters:
    - group_nps (dict): Dictionary with group names as keys and NPS scores as values.

    Returns:
    - fig (matplotlib.figure.Figure): The generated matplotlib figure.
    """
    df = pd.DataFrame(list(group_nps.items()), columns=['Group', 'NPS Score'])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df, x='Group', y='NPS Score', palette='Set3', ax=ax)
    ax.axhline(0, color='gray', linestyle='--')
    ax.set_ylim(-100, 100)
    ax.set_title("NPS Score by Group")
    ax.set_xlabel("Group")
    ax.set_ylabel("NPS Score (%)")
    plt.tight_layout()
    return fig

def plot_aggregated_nps_over_time(model_data):
    """
    Generates a line chart for aggregated NPS over simulation steps.

    Parameters:
    - model_data (pd.DataFrame): DataFrame with 'Overall NPS', 'Promoters %', 'Passives %', 'Detractors %', and 'Group NPS' columns over steps.

    Returns:
    - fig (matplotlib.figure.Figure): The generated matplotlib figure.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(model_data.index, model_data['Overall NPS'], label='Overall NPS', marker='o')

    # Plot Group NPS
    for group in model_data['Group NPS'].iloc[-1].keys():
        ax.plot(model_data.index, model_data['Group NPS'].apply(lambda x: x[group]), label=f'{group} NPS', marker='x')

    ax.axhline(0, color='gray', linestyle='--')
    ax.set_ylim(-100, 100)
    ax.set_title("Aggregated NPS Over Time")
    ax.set_xlabel("Simulation Step")
    ax.set_ylabel("NPS Score (%)")
    ax.legend()
    plt.tight_layout()
    return fig

def plot_final_aggregated_nps(promoters, passives, detractors):
    """
    Generates a pie chart for the final aggregated NPS, including Promoters, Passives, and Detractors.

    Parameters:
    - promoters (float): Percentage of Promoters.
    - passives (float): Percentage of Passives.
    - detractors (float): Percentage of Detractors.

    Returns:
    - fig (matplotlib.figure.Figure): The generated matplotlib figure.
    """
    fig, ax = plt.subplots(figsize=(6, 6))
    labels = ['Promoters', 'Passives', 'Detractors']
    sizes = [promoters, passives, detractors]
    colors = ['#2ecc71', '#f1c40f', '#e74c3c']
    
    # Ensure all sizes are non-negative
    sizes = [max(size, 0) for size in sizes]
    
    # Handle the case where all sizes are zero
    if sum(sizes) == 0:
        sizes = [1, 1, 1]  # Equal distribution to avoid zero division
    
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    ax.set_title("Final Aggregated NPS")
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    return fig