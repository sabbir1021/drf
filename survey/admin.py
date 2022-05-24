from django.contrib import admin
from .models import Survey, SurveyCollector
# Register your models here.
admin.site.register(Survey)
admin.site.register(SurveyCollector)