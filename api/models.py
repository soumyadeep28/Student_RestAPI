from optparse import Option
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Student(models.Model):
    GENDERS = (
        ('m' , 'MALE'),
        ('f' , 'FEMALE'),
        ('d' , 'DISCLOSED')
    )
    name = models.CharField(max_length=250)
    rollnumber = models.IntegerField(unique= True)
    email = models.EmailField(max_length=100)
    gender = models.CharField(choices = GENDERS , max_length=1)
    percentage = models.FloatField()
    Institute = models.ForeignKey('Institute' , on_delete= models.CASCADE)

class Institute(models.Model):
    TYPE = (
        ('s' ,'SCHOOL'),
        ('h' , 'HIGHSCHOOL'),
        ('c' , 'COLLEGE')
    )
    name = models.CharField(max_length=250)
    type_of_Inst = models.CharField(choices= TYPE)