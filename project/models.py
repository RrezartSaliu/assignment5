from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    taken_test = models.IntegerField(blank=True, null=True)


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct = models.CharField(max_length=1)


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

