import streamlit as st
import pandas as pd
import pickle

# ----------------------------
# Load Model + Columns
# ----------------------------
model = pickle.load(open("cost_model.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

# Load dataset (for dynamic dropdowns)
df_dataset = pd.read_csv("medical_cost_dataset.csv")

# ----------------------------
# UI Title
# ----------------------------
st.title("AI-Based Pre-Treatment Cost Prediction System")

# ----------------------------
# Dynamic Disease Selection
# ----------------------------
disease_list = sorted(df_dataset["Disease"].unique())
disease = st.selectbox("Select Disease", disease_list)

# ----------------------------
# Dynamic Treatment Selection
# ----------------------------
treatment_list = sorted(
    df_dataset[df_dataset["Disease"] == disease]["Treatment"].unique()
)
treatment = st.selectbox("Select Treatment", treatment_list)

# ----------------------------
# Other Inputs
# ----------------------------
region = st.selectbox("Select Region", ["North", "South", "East", "West"])
hospital = st.selectbox("Hospital Type", ["Private", "Government"])
smoking = st.selectbox("Smoking Status", ["Yes", "No"])
age = st.number_input("Enter Age", min_value=18, max_value=90)
gender = st.selectbox("Select Gender", ["Male", "Female", "Other"])

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict Treatment Cost"):

    input_dict = {
        "Smoking": 1 if smoking == "Yes" else 0,
        "Age": age
    }

    # Fill encoded columns
    for col in model_columns:

        if col == f"Disease_{disease}":
            input_dict[col] = 1

        elif col == f"Treatment_{treatment}":
            input_dict[col] = 1

        elif col == f"Region_{region}":
            input_dict[col] = 1

        elif col == f"Hospital_Type_{hospital}":
            input_dict[col] = 1

        elif col == f"Gender_{gender}":
            input_dict[col] = 1

        elif col not in input_dict:
            input_dict[col] = 0

    input_df = pd.DataFrame([input_dict])
    input_df = input_df[model_columns]

    prediction = model.predict(input_df)[0]

    st.success(f"Estimated Pre-Treatment Cost: ₹ {int(prediction):,}")
