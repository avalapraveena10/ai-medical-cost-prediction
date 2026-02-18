import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# ----------------------
# Load Dataset
# ----------------------
df = pd.read_csv("medical_cost_dataset.csv")

print(df.head())

# ----------------------
# Preprocessing
# ----------------------

# Convert Smoking to numeric
df['Smoking'] = df['Smoking'].map({'Yes': 1, 'No': 0})

# One Hot Encoding
df = pd.get_dummies(df, columns=[
    'Disease',
    'Treatment',
    'Region',
    'Hospital_Type',
    'Gender'
])

# ----------------------
# Define X and y
# ----------------------
X = df.drop("Cost", axis=1)
y = df["Cost"]

# ----------------------
# Train Test Split
# ----------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training size:", X_train.shape)
print("Testing size:", X_test.shape)

# ----------------------
# Train Model
# ----------------------
model = RandomForestRegressor(
    n_estimators=300,
    max_depth=15,
    random_state=42
)

model.fit(X_train, y_train)

# ----------------------
# Evaluate Model
# ----------------------
predictions = model.predict(X_test)

print("R2 Score:", r2_score(y_test, predictions))
print("MAE:", mean_absolute_error(y_test, predictions))

# ----------------------
# Save Model
# ----------------------
pickle.dump(model, open("cost_model.pkl", "wb"))
pickle.dump(X.columns, open("model_columns.pkl", "wb"))

print("Model saved successfully!")
