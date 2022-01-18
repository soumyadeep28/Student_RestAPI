from django.shortcuts import render
from rest_framework.generics import (ListAPIView ,)

from api import models , serializers


# Create your views here.
class StudentListview(ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class =serializers.StudentSerializers
