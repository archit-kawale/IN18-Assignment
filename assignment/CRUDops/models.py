from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225, null=False)
    email = models.EmailField(max_length=225, null=False)
    DateOfBirth = models.DateField()