import joblib

# Load model
model = joblib.load("best_model.pkl")

# Example prediction
sample_text = "This is a sample input text to classify."
prediction = model.predict([sample_text])

print("Prediction:", "AI" if prediction[0] == 0 else "Human")
