from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.bloghomeView,name='bloghomeView'),
    path('post/<int:id>',views.blogpostView,name='blogpostView'),
]
