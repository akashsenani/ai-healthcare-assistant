from django.shortcuts import render

from .predict import (
    predict_disease,
    symptom_columns
)

from users.models import PredictionHistory

# =====================================================
# PREDICTION PAGE
# =====================================================

def disease_prediction(request):

    results = None

    if request.method == 'POST':

        symptom_text = request.POST.get(
            'symptom_text'
        ).lower()

        # DETECT SYMPTOMS
        selected_symptoms = []

        for symptom in symptom_columns:

            if symptom.lower() in symptom_text:

                selected_symptoms.append(
                    symptom
                )

        # PREDICT
        results = predict_disease(
            selected_symptoms
        )

        # SAVE HISTORY
        if request.user.is_authenticated:

            for result in results:

                PredictionHistory.objects.create(

                    user=request.user,

                    disease=result['disease'],

                    probability=result['probability']
                )

    return render(

        request,

        'prediction.html',

        {
            'results': results
        }
    )