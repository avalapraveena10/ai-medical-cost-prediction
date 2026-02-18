import pandas as pd
import random

# ---------------------------
# Disease → Treatment Mapping
# ---------------------------
disease_treatment = {
    "Heart Disease": ["Angioplasty", "Bypass Surgery", "Stent Placement"],
    "Cancer": ["Chemotherapy", "Radiation Therapy", "Surgery"],
    "Diabetes": ["Insulin Therapy", "Medication Plan", "Monitoring Program"]
}

# ---------------------------
# Base Costs
# ---------------------------
base_cost = {
    "Angioplasty": 150000,
    "Bypass Surgery": 300000,
    "Stent Placement": 200000,
    "Chemotherapy": 250000,
    "Radiation Therapy": 200000,
    "Surgery": 400000,
    "Insulin Therapy": 40000,
    "Medication Plan": 25000,
    "Monitoring Program": 15000
}

regions = ["North", "South", "East", "West"]
hospital_types = ["Private", "Government"]
genders = ["Male", "Female", "Other"]
smoking_status = ["Yes", "No"]

data = []

# ---------------------------
# Generate 3000 records
# ---------------------------
for _ in range(3000):

    disease = random.choice(list(disease_treatment.keys()))
    treatment = random.choice(disease_treatment[disease])
    region = random.choice(regions)
    hospital = random.choice(hospital_types)
    gender = random.choice(genders)
    smoking = random.choice(smoking_status)
    age = random.randint(18, 85)

    cost = base_cost[treatment]

    # Hospital Adjustment
    if hospital == "Private":
        cost *= 1.30
    else:
        cost *= 1.05

    # Smoking Adjustment
    if smoking == "Yes":
        cost *= 1.15

    # Age Adjustment
    if age > 65:
        cost *= 1.20
    elif age > 50:
        cost *= 1.10

    # Region Adjustment
    if region == "North":
        cost *= 1.05
    elif region == "East":
        cost *= 0.97
    elif region == "West":
        cost *= 1.04

    # Add small variation
    cost = cost * random.uniform(0.95, 1.05)

    data.append([
        disease, treatment, region, hospital,
        smoking, age, gender, round(cost)
    ])

# Create DataFrame
columns = [
    "Disease", "Treatment", "Region",
    "Hospital_Type", "Smoking", "Age",
    "Gender", "Cost"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("medical_cost_dataset.csv", index=False)

print("Dataset generated successfully!")
