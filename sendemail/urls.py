from django.urls import path
from sendemail.views import contactView, successView

urlpatterns = [
  
    path('contact/', contactView, name='contact'), 
    path('success/', successView, name='success'),  
    

]
