from django.db import models

# Create your models here.
class Student_info(models.Model):
	st_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=250)
	email= models.EmailField(max_length=140)
	passw = models.CharField(max_length=100)
	