# User Satisfaction and NPS Simulation

This project models user satisfaction and Net Promoter Score (NPS) based on different user personas using the Mesa simulation framework and Streamlit for visualization.

## **Project Structure**

my_simulation_app/
├── app.py
├── simulation/
│   ├── init.py
│   ├── agent.py
│   └── model.py
├── requirements.txt
└── README.md

## **Installation**

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/my_simulation_app.git
   cd my_simulation_app

   2.	Create a Virtual Environment (Optional but Recommended):
   python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


	3.	Install Dependencies:
pip install -r requirements.txt

Running the Application Locally

	1.	Navigate to the Project Directory:
   cd my_simulation_app

	2.	Run the Streamlit App:
   streamlit run app.py

   3.	Access the App:
Open your web browser and navigate to the URL provided in the terminal (typically http://localhost:8501).

Using the Application

	1.	Simulation Parameters:
	•	Number of Users: Set the total number of agents in the simulation.
	•	Number of Simulation Steps: Define how many steps the simulation will run.
	•	CSAT Score: Adjust the Customer Satisfaction score influencing user reactions.
	2.	Persona Initial Satisfaction:
	•	Casuals: Initial satisfaction level for Casual users.
	•	Devs: Initial satisfaction level for Developer users.
	•	Admins: Initial satisfaction level for Admin users.
	3.	Randomness Control:
	•	Random Seed: Set a seed for reproducibility of simulation results.
	4.	Run Simulation:
	•	Click the “Run Simulation” button to execute the simulation with the specified parameters.
	5.	View Results:
	•	Comment Sentiment Counts: View the distribution of user comments.
	•	NPS Score by Persona: See how each persona contributes to the overall NPS.
	•	Aggregated NPS Over Time: Observe how NPS evolves over simulation steps.
	•	Final Aggregated NPS: View the final NPS score after simulation completion.
	6.	Download Results:
	•	Download NPS by Persona as CSV: Export NPS data for further analysis.
	•	Download Final NPS Plot: Save the final NPS visualization as a PNG image.

Deployment

To make your app accessible to others, you can deploy it using Streamlit Sharing or other platforms like Heroku. Below are the steps for deploying with Streamlit Sharing:
	1.	Push Your Code to GitHub:
	•	Ensure your project is in a GitHub repository with the app.py and requirements.txt files.
	2.	Sign Up for Streamlit Sharing:
	•	Visit Streamlit Sharing and sign up or log in.
	3.	Deploy Your App:
	•	Click on “New app”.
	•	Select your GitHub repository and branch.
	•	Specify the path to your app.py (e.g., app.py).
	•	Click “Deploy”.
	4.	Access Your App:
	•	Once deployed, you’ll receive a shareable URL (e.g., https://your-username-my-simulation-app.streamlitapp.com).

Note: Any changes pushed to the GitHub repository will automatically trigger a redeployment, keeping your app up-to-date.

Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

License

This project is licensed under the MIT License.

Contact

For any questions or support, please contact your-email@example.com.

---

## **5. Deployment Instructions**

### **a. Deploying on Streamlit Sharing**

1. **Push Your Code to GitHub:**

   Ensure your project (including `app.py`, `simulation/` directory, and `requirements.txt`) is pushed to a GitHub repository.

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/your-username/my_simulation_app.git
   git branch -M main
   git push -u origin main

   2.	Sign Up/Login to Streamlit Sharing:
Visit Streamlit Sharing and sign up or log in using your GitHub account.
	3.	Deploy Your App:
	•	Click on “New app”.
	•	Select your GitHub repository and the branch you want to deploy from (e.g., main).
	•	Specify the path to your app.py (e.g., app.py).
	•	Click “Deploy”.
	4.	Access Your App:
After deployment, Streamlit will provide a shareable URL where your app is accessible.