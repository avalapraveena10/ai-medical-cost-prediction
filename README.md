AI MEDICAL COST PREDICTION SYSTEM
ABOUT THE PROJECT
This project predicts the estimated medical treatment cost based on patient details like age, BMI, number of children, smoking status, etc.
I built this project to understand how regression models work in real-world healthcare cost estimation.

WHAT I DID:
Loaded and explored the medical cost dataset
Cleaned the data and handled categorical variables
Split the data into training and testing sets
Trained a regression model
Evaluated model performance using R² score
Built a simple Streamlit web interface to make predictions interactive

TECHNOLOGIES USED
Python
Pandas
NumPy
Scikit-learn
Streamlit

MODEL PERFORMANCE
The model was evaluated on test data and achieved a high R² score, showing strong prediction capability.

Clone the repository:
git clone https://github.com/ramakumari1/ai-medical-cost-prediction
cd ai-medical-cost-prediction
pip install -r requirements.txt
streamlit run app.py

EXAMPLE PREDICTION
Input:
Age: 45
BMI: 30
Smoker: Yes
The system predicts the estimated medical cost based on learned patterns from the dataset.

WHAT I LEARNED
Through this project, I improved my understanding of:
Data preprocessing
Regression models
Model evaluation
Building simple ML web apps

