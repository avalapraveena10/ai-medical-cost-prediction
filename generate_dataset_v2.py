import pandas as pd
import random

disease_treatment = {
    "Breast Cancer": {
        "Chemotherapy": 280000,
        "Radiation Therapy": 220000,
        "Surgery": 450000
    },
    "Lung Cancer": {
        "Chemotherapy": 300000,
        "Targeted Therapy": 350000,
        "Surgery": 500000
    },
    "Blood Cancer": {
        "Bone Marrow Transplant": 800000,
        "Chemotherapy": 320000
    },
    "Heart Attack": {
        "Angioplasty": 180000,
        "Bypass Surgery": 320000
    },
    "Heart Blockage": {
        "Stent Placement": 220000,
        "Angioplasty": 170000
    },
    "Type 1 Diabetes": {
        "Insulin Therapy": 60000
    },
    "Type 2 Diabetes": {
        "Medication Plan": 30000,
        "Monitoring Program": 20000
    }
}

regions = ["North", "South", "East", "West"]
hospital_types = ["Private", "Government"]
genders = ["Male", "Female", "Other"]
smoking_status = ["Yes", "No"]

data = []

for _ in range(4000):

    disease = random.choice(list(disease_treatment.keys()))
    treatment = random.choice(list(disease_treatment[disease].keys()))
    cost = disease_treatment[disease][treatment]

    region = random.choice(regions)
    hospital = random.choice(hospital_types)
    gender = random.choice(genders)
    smoking = random.choice(smoking_status)
    age = random.randint(18, 85)

    # Adjustments
    if hospital == "Private":
        cost *= 1.30
    else:
        cost *= 1.05

    if smoking == "Yes":
        cost *= 1.15

    if age > 65:
        cost *= 1.20
    elif age > 50:
        cost *= 1.10

    if region == "North":
        cost *= 1.05
    elif region == "East":
        cost *= 0.97
    elif region == "West":
        cost *= 1.04

    cost = cost * random.uniform(0.95, 1.05)

    data.append([
        disease, treatment, region, hospital,
        smoking, age, gender, round(cost)
    ])

columns = [
    "Disease", "Treatment", "Region",
    "Hospital_Type", "Smoking", "Age",
    "Gender", "Cost"
]

df = pd.DataFrame(data, columns=columns)
df.to_csv("medical_cost_dataset.csv", index=False)

print("New realistic dataset generated!")
