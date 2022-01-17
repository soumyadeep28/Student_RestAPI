from django.urls import path
from api import views

urlpatterns = [ 
    path('viewstudent/' , views.StudentListview.as_view())
]