import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

print("[INFO] Loading dataset from train_and_test2.csv...")
# 1. Dataset Load Karein
df = pd.read_csv("train_and_test2.csv")

# 2. Features aur Target define karein
features = ["Pclass", "Sex", "Age", "sibsp", "Parch", "Fare"]
X = df[features].copy()
y = df["2urvived"]

# 3. Missing values handle karein
X["Age"] = X["Age"].fillna(X["Age"].median())
X["Fare"] = X["Fare"].fillna(X["Fare"].median())

# 4. Train-Test Split (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("[INFO] Training Random Forest model...")
# 5. Model Train Karein
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n[EVALUATION RESULTS]")
print(f"Test Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 7. Model Save Karein
joblib.dump(model, "model.joblib")
print("\n[INFO] Model successfully trained and saved as 'model.joblib'")