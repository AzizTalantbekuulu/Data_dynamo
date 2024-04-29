# analytics_platform/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, EventViewSet, DataViewSet, AnalysisViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'events', EventViewSet)
router.register(r'data', DataViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('analysis/', AnalysisViewSet.as_view({'post': 'analyze_data'}), name='analyze_data'),

]
