from django.db import models

# Create your models here.

class todo(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=50)
