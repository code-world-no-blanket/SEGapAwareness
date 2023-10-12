from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

# Create your models here.


class Skills(models.Model):
    skill_name = models.CharField(max_length=200)
    skill_proficiency = models.IntegerField(default=0)
    skill_guess_proficiency = models.IntegerField(default=0)
    skill_times_practiced = models.IntegerField(default=0)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill_name


class SkillOrderGuess(models.Model):
    skill_guess_array = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(auto_now_add=True)
    question = models.IntegerField(default=0)
    number_wrong = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
