from django.db import models

# Create your models here.
class task(models.Model):

    name = models.CharField(max_length=100)
    priority = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name