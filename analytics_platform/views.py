# analytics_platform/views.py
from rest_framework.response import Response
from rest_framework import viewsets
from .models import User, Event, Data
from .serializers import UserSerializer, EventSerializer, DataSerializer, AnalysisResultSerializer
from .analyzer import analyze_text_data

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class AnalysisViewSet(viewsets.ViewSet):
    def analyze_data(self, request):
        data_id = request.data.get('data_id')
        data = Data.objects.get(id=data_id)
        analysis_result = analyze_text_data(data)
        serializer = AnalysisResultSerializer({'result': analysis_result})
        return Response(serializer.data)