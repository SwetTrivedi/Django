from django.db import models
# Create your models here.
class Lame(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


class Modelinherit(models.Model):
    student_name=models.CharField(max_length=50)
    teacher_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)


#########################################################################

#This is messages framework 

class Messages(models.Model):
    student=models.CharField(max_length=40)
    email=models.CharField(max_length=60)
    password=models.CharField(max_length=50)

