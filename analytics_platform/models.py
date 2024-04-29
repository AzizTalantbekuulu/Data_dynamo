from django.db import models
from django.contrib.auth.models import User as DjangoUser

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Добавьте другие поля, если необходимо

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Добавьте другие поля, если необходимо

class Data(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class AnalysisResult(models.Model):
    data = models.ForeignKey(Data, on_delete=models.CASCADE)
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)