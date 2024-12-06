# simulation/personas.py

class Persona:
    def __init__(self, name, age, experience, attributes):
        """
        Initializes a Persona instance.

        Args:
            name (str): The name of the persona.
            age (int): The age of the persona.
            experience (str): The experience level of the persona.
            attributes (dict): Additional attributes like satisfaction and NPS.
        """
        self.name = name
        self.age = age
        self.experience = experience
        self.attributes = attributes

class Group:
    def __init__(self, name, role, personas):
        """
        Initializes a Group instance.

        Args:
            name (str): The name of the group.
            role (str): The role description of the group.
            personas (list): A list of dictionaries, each representing a persona.
        """
        self.name = name
        self.role = role
        self.personas = [Persona(**persona) for persona in personas]

# Define the groups and their personas
PERSONAS = {
    "Business Specialist": {
        "role": "The Business Specialist often has specialist skills, knowledge, and experience when working with data to provide analysis, support, or drive decision-making with analytics in the organization. Even though many of these people are focused and skilled in working on data, their role and ambition are to support business with analytics.",
        "personas": [
            {
                "name": "Operational Worker",
                "age": 30,
                "experience": "5 years",
                "attributes": {
                    "satisfaction": 7,
                    "nps": 8
                }
            },
            {
                "name": "Business Manager",
                "age": 40,
                "experience": "15 years",
                "attributes": {
                    "satisfaction": 8,
                    "nps": 9
                }
            },
            {
                "name": "Company Executive",
                "age": 50,
                "experience": "25 years",
                "attributes": {
                    "satisfaction": 9,
                    "nps": 10
                }
            }
        ]
    },
    "Business Casual": {
        "role": "The Business Casual is at the end of the value chain, often with little time, skill, or motivation to work with data on their own. Instead, they depend on reliable and actionable information to use when executing their job of running the business. They are often the business leaders responsible for business functions or conducting operational tasks in the business.",
        "personas": [
            {
                "name": "Business Analyst",
                "age": 35,
                "experience": "10 years",
                "attributes": {
                    "satisfaction": 6,
                    "nps": 7
                }
            },
            {
                "name": "Analytics Developer",
                "age": 32,
                "experience": "8 years",
                "attributes": {
                    "satisfaction": 7,
                    "nps": 8
                }
            },
            {
                "name": "Analytics Engineer",
                "age": 38,
                "experience": "12 years",
                "attributes": {
                    "satisfaction": 7,
                    "nps": 8
                }
            },
            {
                "name": "Solution Architect",
                "age": 45,
                "experience": "20 years",
                "attributes": {
                    "satisfaction": 8,
                    "nps": 9
                }
            },
            {
                "name": "Data Scientist",
                "age": 33,
                "experience": "9 years",
                "attributes": {
                    "satisfaction": 8,
                    "nps": 9
                }
            }
        ]
    },
    "Data Expert": {
        "role": "The Data Expert focuses on acquiring, creating, validating, storing, protecting, transforming, and processing data to ensure the accessibility, reliability, fitness, and timeliness of such data for use within the organization.",
        "personas": [
            {
                "name": "Data Architect",
                "age": 42,
                "experience": "18 years",
                "attributes": {
                    "satisfaction": 9,
                    "nps": 10
                }
            },
            {
                "name": "Data Engineer",
                "age": 36,
                "experience": "12 years",
                "attributes": {
                    "satisfaction": 8,
                    "nps": 9
                }
            },
            {
                "name": "Transformation Specialist",
                "age": 39,
                "experience": "14 years",
                "attributes": {
                    "satisfaction": 8,
                    "nps": 9
                }
            },
            {
                "name": "Onboarding Specialist",
                "age": 29,
                "experience": "6 years",
                "attributes": {
                    "satisfaction": 7,
                    "nps": 8
                }
            },
            {
                "name": "Data Steward",
                "age": 40,
                "experience": "16 years",
                "attributes": {
                    "satisfaction": 8,
                    "nps": 9
                }
            },
            {
                "name": "Data Product Manager",
                "age": 37,
                "experience": "13 years",
                "attributes": {
                    "satisfaction": 8,
                    "nps": 9
                }
            }
        ]
    },
    "System Expert": {
        "role": "The System Expert is an expert on creating and managing systems, data, and technology solutions for others in the organization to use as a platform for other data and analytics jobs along the value chain.",
        "personas": [
            {
                "name": "Enterprise Architect",
                "age": 45,
                "experience": "20 years",
                "attributes": {
                    "satisfaction": 9,
                    "nps": 10
                }
            },
            {
                "name": "Software Engineer",
                "age": 30,
                "experience": "7 years",
                "attributes": {
                    "satisfaction": 7,
                    "nps": 8
                }
            },
            {
                "name": "System and Database Admin",
                "age": 35,
                "experience": "10 years",
                "attributes": {
                    "satisfaction": 8,
                    "nps": 9
                }
            },
            {
                "name": "System Operator",
                "age": 28,
                "experience": "5 years",
                "attributes": {
                    "satisfaction": 6,
                    "nps": 7
                }
            },
            {
                "name": "DataOps",
                "age": 34,
                "experience": "9 years",
                "attributes": {
                    "satisfaction": 8,
                    "nps": 9
                }
            }
        ]
    }
}