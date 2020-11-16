from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.indexView,name="indexView"),
    path('saveView',views.saveView,name="saveView"),
    path('editView',views.editView,name="editView"),
    path('deleteView',views.deleteView,name="deleteView")
]