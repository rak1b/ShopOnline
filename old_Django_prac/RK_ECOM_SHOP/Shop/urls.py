from . import views
from django.urls import path

urlpatterns = [
	path('', views.Shop_View,name='Shop_View'),

]