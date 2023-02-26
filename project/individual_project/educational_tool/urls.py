from django.urls import path
from educational_tool import views

#manually created this file 
app_name = 'educational_tool'

urlpatterns = [
path('', views.index, name='index'),
path('about/', views.about, name='about'),
path('category/<slug:category_name_slug>/',views.show_category, name='show_category'),
path('pycompiler/', views.pycompiler, name='pycompiler'),
path('register/', views.register, name='register'),
path('login/', views.user_login, name='login'),
path('videos/', views.video , name='videos'),
 path('videos/<str:video_id>', views.show_video, name='show_video'),
# path('runcode', views.runcode, name='runcode'),

]
