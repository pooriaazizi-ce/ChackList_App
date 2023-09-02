from django.db import models
import datetime

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=True,blank=False)
    start_date = models.CharField(max_length=200,blank=True)
    end_date = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.item+' | '+self.completed

