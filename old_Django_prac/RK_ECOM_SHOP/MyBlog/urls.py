from . import views
from django.urls import path

urlpatterns = [
	path('', views.Blog_View,name='Blog_View'),

]