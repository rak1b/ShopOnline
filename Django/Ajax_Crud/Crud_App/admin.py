from django.contrib import admin
from .models import Student_info

# Register your models here.
@admin.register(Student_info)
class Student_info_Admin(admin.ModelAdmin):
	list_display=('st_id','name','email','passw')

# admin.site.register(Student_info,Student_info_Admin)