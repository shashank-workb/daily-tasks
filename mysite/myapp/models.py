from django.db import models
from datetime import datetime
# Create your models here.
class task(models.Model):

    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    priority = models.IntegerField(default=5)
    date = models.DateTimeField(default=datetime.now)

