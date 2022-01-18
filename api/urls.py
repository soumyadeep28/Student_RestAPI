from django.urls import path
from api import views

urlpatterns = [ 
    path('viewstudent/' , views.StudentListview.as_view()),
    path('detailstudent/<int:pk>' , views.StudentDetailview.as_view()),
    path('viewcreatestudent/' , views.StudenlistCreate.as_view()),
    path('updatestudent/<int:pk>' , views.StudentUpdateview.as_view()),
    path('deletestudent/<int:pk>' , views.Deletestudent.as_view())

]