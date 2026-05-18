from django.db import models

from django.contrib.auth.models import User

# =====================================================
# USER PROFILE MODEL
# =====================================================

class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    age = models.IntegerField(
        null=True,
        blank=True
    )

    weight = models.FloatField(
        null=True,
        blank=True
    )

    height = models.FloatField(
        null=True,
        blank=True
    )

    bmi = models.FloatField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.user.username
    

# =====================================================
# BMI HISTORY
# =====================================================

class BMIHistory(models.Model):

    user = models.ForeignKey(

        User,

        on_delete=models.CASCADE
    )

    bmi = models.FloatField()

    created_at = models.DateTimeField(

        auto_now_add=True
    )

    def __str__(self):

        return f"{self.user.username} - {self.bmi}"
# =====================================================
# DISEASE PREDICTION HISTORY
# =====================================================

class PredictionHistory(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    disease = models.CharField(
        max_length=255
    )

    probability = models.FloatField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

# =====================================================
# CHATBOT HISTORY
# =====================================================

class ChatbotHistory(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    question = models.TextField()

    response = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )