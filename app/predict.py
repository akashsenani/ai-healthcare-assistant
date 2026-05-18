import joblib
import numpy as np
import pandas as pd

# LOAD FILES
model = joblib.load("models/disease_prediction_model.pkl")
label_encoder = joblib.load("models/label_encoder.pkl")
symptom_columns = joblib.load("models/symptom_columns.pkl")


def predict_disease(selected_symptoms):

    # Create empty symptom vector
    input_data = np.zeros(len(symptom_columns))

    # Set selected symptoms = 1
    for symptom in selected_symptoms:
        if symptom in symptom_columns:
            index = symptom_columns.index(symptom)
            input_data[index] = 1

    # Convert to dataframe
    input_df = pd.DataFrame(
        [input_data],
        columns=symptom_columns
    )

    # Predict probabilities
    probabilities = model.predict_proba(input_df)[0]

    # Top 5 predictions
    top5_indices = np.argsort(probabilities)[-5:][::-1]

    results = []

    for idx in top5_indices:
        disease = label_encoder.inverse_transform([idx])[0]
        probability = probabilities[idx]

        results.append({
            "disease": disease,
            "probability": round(float(probability) * 100, 2)
        })

    return results
