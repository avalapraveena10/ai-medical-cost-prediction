###### &#x20;**AI-Based Pre-Treatment Medical Cost Prediction System**



###### &#x20;Project Overview



The **AI-Based Pre-Treatment Medical Cost Prediction System** is a Machine Learning application that predicts the estimated cost of medical treatment based on patient and treatment-related information.



The system uses a **Random Forest Regression** model and provides an interactive **Streamlit web application** where users can enter patient details and receive an estimated pre-treatment cost.



&#x20;**Problem Statement**



Medical treatment costs can vary significantly depending on factors such as disease, treatment type, patient age, smoking status, gender, region, and hospital type.



This project aims to provide an estimated treatment cost before treatment begins by analyzing these factors using a Machine Learning regression model.



**Note:**The prediction is an estimate generated from the project's dataset and should not be considered an actual medical or financial quotation.



&#x20;**Features**



\- Predicts estimated pre-treatment medical costs

\- Interactive Streamlit web interface

\- Disease-based treatment selection

\- Handles categorical variables using one-hot encoding

\- Converts smoking status into numerical values

\- Random Forest Regression model

\- Model evaluation using R² Score and Mean Absolute Error

\- Trained model saved using Python Pickle

\- Git LFS used for the large trained model file



&#x20;**Machine Learning Model**



The project uses:



###### **Random Forest Regressor**



Model configuration:



\- Number of estimators: 300

\- Maximum depth: 15

\- Random state: 42

\- Test size: 20%



###### **Data Preprocessing**



The following preprocessing steps are performed:



1\. Smoking status is converted into numerical values:

&#x20;  - Yes → 1

&#x20;  - No → 0



2\. One-hot encoding is applied to:

&#x20;  - Disease

&#x20;  - Treatment

&#x20;  - Region

&#x20;  - Hospital Type

&#x20;  - Gender



3\. The dataset is divided into:

&#x20;  - 80% training data

&#x20;  - 20% testing data



###### 📊 **Model Performance**



The model was evaluated on **800 test samples**.



| Metric                 | Result |

|------------------------|------: |

| Training Samples       | 3,200  |

| Testing Samples        | 800    |

| Features After Encoding| 29     |

| R² Score               | 0.99684|

| Mean Absolute Error    |₹9,778.91|



The R² score of **0.99684** indicates that the model explains approximately **99.68%** of the variance in the target values on this particular test split.



The MAE of approximately **₹9,779** represents the average absolute difference between predicted and actual costs on the test set.



> **Important:**These results are based on this project's dataset and test split. They should not be interpreted as real-world medical cost accuracy.



###### &#x20;**Streamlit Application**



The application collects the following inputs:



\- Disease

\- Treatment

\- Region

\- Hospital Type

\- Smoking Status

\- Age

\- Gender



After clicking **Predict Treatment Cost**, the trained Random Forest model generates an estimated pre-treatment cost.



Example output:



text

Estimated Pre-Treatment Cost: ₹ 394,704

