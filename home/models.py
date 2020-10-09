from django.db import models
from datetime import datetime

class Exam(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now(), blank=True)


class Question(models.Model):
    title = models.CharField(max_length=200)
    Option1 = models.CharField(max_length=200)
    Option2 = models.CharField(max_length=200)
    Option3 = models.CharField(max_length=200)
    Option4 = models.CharField(max_length=200)
    CorrectOption = models.CharField(max_length=100)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

