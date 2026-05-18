from predict import predict_disease

# Example symptoms
symptoms = [
    "fever",
    "headache",
    "vomiting"
]

# Predict
results = predict_disease(symptoms)

# Print results
print("\nTop Disease Predictions:\n")

for item in results:
    print(
        f"{item['disease']} --> {item['probability']}%"
    )