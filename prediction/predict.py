import joblib
import pandas as pd
import numpy as np

# =====================================================
# LOAD MODEL FILES
# =====================================================

model = joblib.load(
    "models/disease_prediction_model.pkl"
)

label_encoder = joblib.load(
    "models/label_encoder.pkl"
)

symptom_columns = joblib.load(
    "models/symptom_columns.pkl"
)

# =====================================================
# PREDICT FUNCTION
# =====================================================

def predict_disease(selected_symptoms):

    # Create input vector
    input_data = np.zeros(
        len(symptom_columns)
    )

    # Mark selected symptoms
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
    probabilities = model.predict_proba(
        input_df
    )[0]

    # Top predictions
    top_indices = np.argsort(
        probabilities
    )[-5:][::-1]

    results = []

    for idx in top_indices:

        disease = label_encoder.inverse_transform(
            [idx]
        )[0]

        probability = round(
            probabilities[idx] * 100,
            2
        )

        results.append({

            "disease": disease,
            "probability": probability
        })

    return results