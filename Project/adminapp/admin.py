from django.contrib import admin
from .models import Conversation, PredictionHistory

# Register Conversation model
admin.site.register(Conversation)

# Register PredictionHistory model
admin.site.register(PredictionHistory)
# Register your models here.
