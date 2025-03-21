from django.db import models
from userapp.models import User  # or wherever your User model is located

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user_message = models.TextField()
    bot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user_message[:50]}..."
    


import json
from django.db import models
from django.utils.timezone import now

class PredictionHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input_text = models.TextField(verbose_name="User Input")
    prediction_result = models.CharField(max_length=100, verbose_name="Prediction Result")
    timestamp = models.DateTimeField(default=now, verbose_name="Prediction Time")
    
    # Store up to 5 YouTube video links for music therapy
    music_therapy_links = models.JSONField(default=list, blank=True, verbose_name="Music Therapy Links")

    # Store a workout plan as a paragraph
    guided_workout_plan = models.TextField(blank=True, verbose_name="Guided Workout Plan")

    class Meta:
        db_table = "user_predictions"

    def music_therapy_links_json(self):
        return json.dumps(self.music_therapy_links)

    def __str__(self):
        return f"{self.user.full_name} - {self.prediction_result}"
