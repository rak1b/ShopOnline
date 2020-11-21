from django.db import models

# Create your models here.
class Blog_Post(models.Model):
	post_id = models.AutoField(primary_key = True)
	post_name = models.CharField(max_length=200)
	post_desc = models.CharField(max_length=1000)
	post_date = models.DateField(auto_now_add =True)
