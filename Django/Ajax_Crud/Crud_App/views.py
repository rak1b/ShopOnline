from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
# from .forms import Student_info_forms
# import Crud_App.forms
from .forms import myform
from .models import Student_info

# Create your views here.

def successView(request):
	return render(request,'success.html')

def delete_data(request,id):
	val = Student_info.objects.get(st_id = id)
	val.delete()
	return HttpResponseRedirect('/')


def homeView(request):
	# form = Student_info()
	# form = myform(auto_id='Rk%s')
	form = myform(auto_id=True)

	if(request.method=="POST"):
		form = myform(request.POST)
		# print('Got From Post:',form)
		if form.is_valid():
			print(form.cleaned_data)
			name =form.cleaned_data['name']
			email =form.cleaned_data['email']
			age =form.cleaned_data['age']
			password =form.cleaned_data['password']
			print(name)
			print(email)
			print(age)
			# return HttpResponseRedirect("/success")
			# return render(request,'success.html',{'name':name})
			# return redirect('successView',{'name':name})

			st = Student_info(name=name,email=email,passw=password)
			st.save()

	students = Student_info.objects.all()

	return render(request,'index.html',{'fm':form,'student':students})  
