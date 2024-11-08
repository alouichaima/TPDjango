from django.urls import path

from MyContact import views

urlpatterns = [
    path('form1', views.controlform1, name='controlform1'),  
    path('form2', views.controleform2, name='controleform2'),  
    path('form3', views.controleform3, name='controleform3'),  



]