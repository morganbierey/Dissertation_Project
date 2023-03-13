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
path('video/<v_id>/',views.show_video, name='show_video'),
path('compilerbase/<p_id>/', views.compilerbase, name='compilerbase'),
path('tutorial/<tut_id>/', views.show_tutorial, name='tutorial'),
path('topic/<t_id>/', views.show_topic, name='show_topic'),
path('base/', views.base, name='base'),
path('logout/', views.user_logout, name='logout'),
path('profile/', views.view_profile, name='profile')


# path('runcode', views.runcode, name='runcode'),


]
