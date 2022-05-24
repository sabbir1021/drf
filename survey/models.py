from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Survey(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class SurveyCollector(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.survey ) + "-----------" + str(self.user )