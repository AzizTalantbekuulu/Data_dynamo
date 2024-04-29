from django.contrib import admin
from .models import User, Event, Data, AnalysisResult


admin.site.register(User)
admin.site.register(Event)
admin.site.register(Data)
admin.site.register(AnalysisResult)