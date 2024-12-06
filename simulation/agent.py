# simulation/agent.py

from mesa import Agent

class UserAgent(Agent):
    def __init__(self, unique_id, model, group, persona):
        """
        Initializes a UserAgent.

        Args:
            unique_id (int): Unique identifier for the agent.
            model (UserModel): Reference to the simulation model.
            group (Group): The group to which the agent belongs.
            persona (Persona): The persona assigned to the agent.
        """
        super().__init__(unique_id, model)
        self.group = group
        self.persona = persona
        self.satisfaction = persona.attributes.get('satisfaction', 5)
        self.nps = persona.attributes.get('nps', 0)
        self.comment = ""
        self.sentiment = "Neutral"

    def step(self):
        """
        Defines the agent's behavior for each simulation step.
        """
        self.update_satisfaction()
        self.update_nps()
        self.generate_comment()

    def update_satisfaction(self):
        """
        Updates the agent's satisfaction based on certain conditions or interactions.
        """
        # Example Logic: Random fluctuation in satisfaction
        change = self.random.choice([-1, 0, 1])
        self.satisfaction = max(0, min(10, self.satisfaction + change))

    def update_nps(self):
        """
        Updates the agent's NPS based on satisfaction.
        """
        # Simple Mapping: Higher satisfaction leads to higher NPS
        if self.satisfaction >= 9:
            self.nps = 10
        elif 7 <= self.satisfaction <= 8:
            self.nps = 8
        elif 5 <= self.satisfaction <= 6:
            self.nps = 6
        elif 3 <= self.satisfaction <= 4:
            self.nps = 4
        else:
            self.nps = 2

    def generate_comment(self):
        """
        Generates a comment based on satisfaction and analyzes sentiment.
        """
        if self.satisfaction >= 8:
            self.comment = "Great service!"
            self.sentiment = "Positive"
        elif 5 <= self.satisfaction <= 7:
            self.comment = "I'm okay with the current state."
            self.sentiment = "Neutral"
        else:
            self.comment = "I'm not satisfied with the recent changes."
            self.sentiment = "Negative"