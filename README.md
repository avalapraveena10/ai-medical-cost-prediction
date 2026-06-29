
###  AI Medical Cost Prediction System ###


### About the Project

This project predicts estimated medical insurance costs based on patient information such as age, BMI, smoking status, number of children, and region. It uses a Machine Learning regression model and provides predictions through a simple Streamlit web application.

### Features:

Predicts medical insurance costs
Interactive Streamlit web interface
Data preprocessing and feature encoding
Machine Learning regression model
Real-time cost prediction


### Tech Stack
Python
Pandas
NumPy
Scikit-learn
Streamlit


### Project Workflow
Load and preprocess the dataset
Handle categorical variables
Split data into training and testing sets
Train the regression model
Evaluate model performance
Predict medical costs using Streamlit

### Model Performance

The regression model achieved a strong R² Score on the test dataset, demonstrating good prediction accuracy.

 ### Installation
git clone https://github.com/ramakumari1/ai-medical-cost-prediction
cd ai-medical-cost-prediction
pip install -r requirements.txt
streamlit run app.py


### Example Prediction:
Input	Value
Age	45
BMI	30
Smoker	Yes

Output: Estimated Medical Insurance Cost

### What I Learned:

Data preprocessing
Feature engineering
Regression algorithms
Model evaluation
Building Machine Learning web applications using Streamlit


### Future Enhancements
Deploy the application online
Support multiple regression models
Improve prediction accuracy using hyperparameter tuning
Add data visualization dashboard
