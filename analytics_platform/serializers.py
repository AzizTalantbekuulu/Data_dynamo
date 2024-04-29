from rest_framework import serializers
from .models import User, Event, Data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'user', 'event_type', 'timestamp']

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['id', 'name', 'description', 'uploaded_by', 'created_at']

class AnalysisResultSerializer(serializers.Serializer):
    result = serializers.CharField()