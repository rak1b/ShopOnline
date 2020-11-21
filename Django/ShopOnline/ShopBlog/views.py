from django.shortcuts import render
from django.http import request
from ShopBlog.models import Blog_Post


# Create your views here.
def bloghomeView(request):
	post = Blog_Post.objects.all()
	return render(request,'blog/home.html',{'post':post})

def blogpostView(request,id):
	p = Blog_Post.objects.filter(post_id=id)
	print(p)
	for i in p:
		print(i.post_id)
	# 
	return render(request,'blog/post.html',{'post':p})