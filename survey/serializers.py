from rest_framework import serializers
from .models import SurveyCollector

class SurveyCollectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = SurveyCollector
        fields = "__all__"
    