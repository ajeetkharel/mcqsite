from django.db import models

class Exam(models.Model):
    Question = models.CharField(max_length=200)
    Option1 = models.CharField(max_length=200)
    Option2 = models.CharField(max_length=200)
    Option3 = models.CharField(max_length=200)
    Option4 = models.CharField(max_length=200)
    CorrectOption = models.CharField(max_length=100)

