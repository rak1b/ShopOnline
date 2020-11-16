# from django.contrib import admin
# from django.urls import path,include
# from . import views

# urlpatterns = [
#     path('',views.indexView,name="indexView"),
#     path('processView/',views.processView,name='processView')

# ]

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index), 
    path('second/', views.second,name='second'), 
    path('ajax-posting/', views.ajax_posting, name='ajax_posting'),# ajax-posting / name = that we will use in ajax url
    path('second_ajax_posting/', views.second_ajax_posting, name='second_ajax_posting'),# ajax-posting / name = that we will use in ajax url
    path('third',views.third,name="third"),
    path('third_ajax',views.third_ajax,name="third_ajax")
]


