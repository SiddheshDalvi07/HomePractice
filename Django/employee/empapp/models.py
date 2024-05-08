from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.fname