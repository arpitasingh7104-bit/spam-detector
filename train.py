import pandas as pd, joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("spam.csv")
X_train, X_test, y_train, y_test = train_test_split(
    df["message"], df["label"], test_size=0.2, random_state=42, stratify=df["label"]
)

model = make_pipeline(TfidfVectorizer(stop_words="english"), MultinomialNB())
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, pred), 3))
print(classification_report(y_test, pred))
print("Confusion matrix (rows = actual, columns = predicted: ham, spam):")
print(confusion_matrix(y_test, pred, labels=["ham", "spam"]))

joblib.dump(model, "model.pkl")
print("Model saved to model.pkl")