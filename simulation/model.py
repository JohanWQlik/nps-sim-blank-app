# simulation/model.py

from dataclasses import dataclass
from mesa import Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from .personas import Group, Persona, PERSONAS
from .agent import UserAgent

@dataclass
class Change:
    """
    A data class to encapsulate simulation change parameters.
    
    Attributes:
        csat_score (float): The Customer Satisfaction Score influencing the simulation.
    """
    csat_score: float

class UserModel(Model):
    def __init__(self, num_users, change: Change, initial_satisfaction: dict):
        """
        Initializes the UserModel.
        
        Args:
            num_users (int): Number of user agents in the simulation.
            change (Change): An object representing changes in satisfaction or other parameters.
            initial_satisfaction (dict): A dictionary mapping persona names to their initial satisfaction levels.
        """
        self.num_users = num_users
        self.schedule = RandomActivation(self)
        self.change = change  # Incorporates change parameters into the model
        self.datacollector = DataCollector(
            model_reporters={
                "Overall NPS": self.compute_overall_nps,
                "Promoters %": self.compute_promoters_percentage,
                "Passives %": self.compute_passives_percentage,
                "Detractors %": self.compute_detractors_percentage,
                "Group NPS": self.compute_group_nps
            },
            agent_reporters={
                "Group": "group.name",
                "Persona": "persona.name",
                "NPS Rating": "nps"
            }
        )
        
        # Initialize groups and personas
        self.groups = [Group(name, details["role"], details["personas"]) for name, details in PERSONAS.items()]
        
        # Initialize agents
        for i in range(self.num_users):
            group = self.random.choice(self.groups)
            persona = self.random.choice(group.personas)
            agent = UserAgent(i, self, group, persona)
            # Set initial satisfaction based on UI inputs
            agent.satisfaction = initial_satisfaction.get(persona.name, persona.attributes.get('satisfaction', 5))
            agent.nps = persona.attributes.get('nps', 0)
            self.schedule.add(agent)
        
        self.comments = []  # Initialize comments list
        self.datacollector.collect(self)  # Collect initial data

    def step(self):
        """
        Advances the simulation by one step.
        """
        self.schedule.step()
        self.datacollector.collect(self)
        self.collect_comments()

    def collect_comments(self):
        """
        Collects comments from all agents and stores them in the comments list.
        """
        for agent in self.schedule.agents:
            if hasattr(agent, 'comment') and hasattr(agent, 'sentiment'):
                self.comments.append({
                    "agent_id": agent.unique_id,
                    "group": agent.group.name,
                    "persona": agent.persona.name,
                    "comment": agent.comment,
                    "sentiment": agent.sentiment
                })

    def compute_overall_nps(self):
        """
        Computes the overall NPS across all agents.
        
        Returns:
            float: The overall NPS score.
        """
        promoters = detractors = total = 0
        for agent in self.schedule.agents:
            total += 1
            if agent.nps >= 9:
                promoters += 1
            elif agent.nps <= 6:
                detractors += 1
        return ((promoters - detractors) / total) * 100 if total > 0 else 0

    def compute_promoters_percentage(self):
        """
        Computes the percentage of Promoters in the simulation.
        
        Returns:
            float: Percentage of Promoters.
        """
        promoters = sum(1 for agent in self.schedule.agents if agent.nps >= 9)
        return (promoters / self.num_users) * 100 if self.num_users > 0 else 0

    def compute_passives_percentage(self):
        """
        Computes the percentage of Passives in the simulation.
        
        Returns:
            float: Percentage of Passives.
        """
        passives = sum(1 for agent in self.schedule.agents if 7 <= agent.nps <= 8)
        return (passives / self.num_users) * 100 if self.num_users > 0 else 0

    def compute_detractors_percentage(self):
        """
        Computes the percentage of Detractors in the simulation.
        
        Returns:
            float: Percentage of Detractors.
        """
        detractors = sum(1 for agent in self.schedule.agents if agent.nps <= 6)
        return (detractors / self.num_users) * 100 if self.num_users > 0 else 0

    def compute_group_nps(self):
        """
        Computes the NPS for each group.
        
        Returns:
            dict: A dictionary mapping group names to their respective NPS scores.
        """
        group_nps = {}
        for group in self.groups:
            promoters = detractors = total = 0
            for agent in self.schedule.agents:
                if agent.group.name == group.name:
                    total += 1
                    if agent.nps >= 9:
                        promoters += 1
                    elif agent.nps <= 6:
                        detractors += 1
            group_nps[group.name] = ((promoters - detractors) / total) * 100 if total > 0 else 0
        return group_nps