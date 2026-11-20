from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Breast Cancer Classification completed")
print("Dataset shape:", X.shape)
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))
print("Accuracy:", accuracy_score(y_test, predictions))
print("Class names:", list(data.target_names))
print("Number of features:", len(data.feature_names))
