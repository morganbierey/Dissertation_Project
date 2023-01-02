from django.urls import path
from educational_tool import views

#manually created this file 
app_name = 'educational_tool'

urlpatterns = [
path('', views.index, name='index'),
<<<<<<< HEAD
path('about/', views.about, name='about'),
=======
>>>>>>> da5efec9b488fb10c2988553e0965ca90b006e08
]
