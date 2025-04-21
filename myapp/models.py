from django.db import models


#Storing Studends Details
class StudentCallList(models.Model):
    Your_Name = models.CharField(max_length=1000)
    Email =models.EmailField(max_length=100)
    Mobile_No = models.IntegerField()
    City = models.CharField(max_length=1000)
    College_Name = models.CharField(max_length=1000)
    Department = models.CharField(max_length=1000)