from django.db import models

# Create your models here.
class Example(models.Model):
    username=models.CharField(max_length=20)
    age=models.IntegerField()
