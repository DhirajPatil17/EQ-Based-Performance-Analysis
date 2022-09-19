from django.db import models

class visualize(models.Model):
  
    Name=models.CharField(max_length=50)
    Marks=models.IntegerField()
    Attendence=models.IntegerField()
    Behavioral=models.IntegerField()
class Fyit(models.Model):
   Name=models.CharField(max_length=50)
   Marks=models.IntegerField()
   Attendence=models.IntegerField()
   Behavioral=models.IntegerField()
class Syit(models.Model):
   Name=models.CharField(max_length=50)
   Marks=models.IntegerField()
   Attendence=models.IntegerField()
   Behavioral=models.IntegerField()


