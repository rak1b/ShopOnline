from django.contrib import admin
from ShopBlog.models import Blog_Post
# Register your models here

@admin.register(Blog_Post)
class Blog_PostAdmin(admin.ModelAdmin):
	list_display = [
		'post_id',
		'post_name',
		'post_desc',
		'post_date'
	]