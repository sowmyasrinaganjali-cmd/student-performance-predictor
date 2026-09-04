import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# 1. Load the dataset
data = pd.read_csv("data/student_data.csv")


# 2. Select the input features
X = data[
    [
        "study_hours",
        "previous_score",
        "attendance",
        "sleep_hours",
        "assignments_completed",
        "participation"
    ]
]


# 3. Select what we want to predict
y = data["final_score"]


# 4. Split the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 5. Create the machine learning model
model = LinearRegression()


# 6. Train the model
model.fit(X_train, y_train)


# 7. Make predictions
predictions = model.predict(X_test)


# 8. Check the model performance
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model Training Completed!")
print("-------------------------")
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))


# 9. Show actual and predicted scores
print("\nActual vs Predicted Scores:")

for actual, predicted in zip(y_test, predictions):
    print(
        "Actual:",
        actual,
        "| Predicted:",
        round(predicted, 2)
    )


# 10. Save the trained model
joblib.dump(
    model,
    "model/student_performance_model.pkl"
)

print("\nModel saved successfully!")