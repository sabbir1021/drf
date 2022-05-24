from django.urls import path
from . import views

urlpatterns = [
    path('survey-collector/', views.SurveyCollectorList.as_view(), name = "survey-collector")
]