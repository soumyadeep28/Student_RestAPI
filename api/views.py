from django.shortcuts import render
from rest_framework.generics import (ListAPIView , RetrieveAPIView ,ListCreateAPIView , RetrieveUpdateAPIView ,
DestroyAPIView ,RetrieveUpdateDestroyAPIView )
# RetrieveUpdateDestroyAPIView makes the code all the operation in one 

from api import models , serializers


# Create your views here.
class StudentListview(ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class =serializers.StudentSerializers

#if post then update else view all 
class StudenlistCreate(ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializers

class StudentDetailview(RetrieveAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializers

#this is for update or fetch the details if patch then update the column
class StudentUpdateview(RetrieveUpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializers

#to test this use delete operations 
class Deletestudent(DestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializers







