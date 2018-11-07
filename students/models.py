from django.db import models
from datetime import datetime

# Create your models here.


class Student(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    enrolled_at = models.DateTimeField(default=datetime.now(), blank=True)
    gpa = models.IntegerField()

    def __str__(self):
        return "{}, {}".format(self.last_name, self.first_name)
