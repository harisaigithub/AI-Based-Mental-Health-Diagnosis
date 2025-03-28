from django.contrib import admin
from django.contrib import admin
from .models import User, FeedbackModel

# Register User model
admin.site.register(User)

# Register FeedbackModel model
admin.site.register(FeedbackModel)
# Register your models here.
