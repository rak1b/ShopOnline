from django.db import models

# Create your models here.

class Student(models.Model):
	st_id = models.AutoField(primary_key=True)
	st_name = models.CharField(max_length=200)
	st_email = models.CharField(max_length=200)
	st_pass = models.CharField(max_length=200)