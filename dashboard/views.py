from django.shortcuts import render

from users.models import (
    UserProfile,
    PredictionHistory,
    BMIHistory
)

# =====================================================
# DASHBOARD
# =====================================================

def dashboard_view(request):

    bmi = 0

    total_predictions = 0

    chart_labels = []

    chart_values = []

    if request.user.is_authenticated:

        # USER PROFILE
        try:

            profile = UserProfile.objects.get(

                user=request.user
            )

            bmi = profile.bmi

        except:

            bmi = 0

        # TOTAL PREDICTIONS
        total_predictions = PredictionHistory.objects.filter(

            user=request.user

        ).count()

        # BMI HISTORY
        bmi_records = BMIHistory.objects.filter(

            user=request.user

        ).order_by('created_at')

        # DEBUG PRINT
        print(bmi_records)

        for record in bmi_records:

            chart_labels.append(

                record.created_at.strftime(
                    "%d %b %H:%M"
                )
            )

            chart_values.append(
                float(record.bmi)
            )

    context = {

        'bmi': bmi,

        'total_predictions':
            total_predictions,

        'chart_labels':
            chart_labels,

        'chart_values':
            chart_values
    }

    return render(

        request,

        'dashboard.html',

        context
    )