from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentForm
from .models import Student
from django.http import JsonResponse

# Create your views here.
def deleteView(request):
	if request.is_ajax():
		id = request.POST.get('id',None)
		if id:

			student =Student.objects.get(st_id=id)
			student.delete()
			response={
				'info':'Deleted successfully'
			}

		return JsonResponse(response)


def editView(request):
	if(request.is_ajax()):
		myid = request.POST.get('id',None)
		if myid:
			st = Student.objects.get(st_id = myid)
			# std = list(st)
			print(myid)
			print(st.st_pass)
			response = {
				'info':"success",
				'id':st.st_id,
				'name':st.st_name,
				'email':st.st_email,
				'password':st.st_pass,
			}
	

		return JsonResponse(response)

def saveView(request):
	if(request.is_ajax()):
		name = request.POST.get('nm',None)
		email = request.POST.get('em',None)
		password = request.POST.get('pd',None)
		this_id = request.POST.get('id')
		print(name)
		print(email)
		print(password)
		print("In save View")
		if name and email and password and this_id=='':
			# print("none")
			st = Student(st_name = name,st_email=email,st_pass=password)
			st.save()
		else:
			# print("something")
			st = Student(st_id = this_id,st_name = name,st_email=email,st_pass=password)
			st.save()

		student_data = Student.objects.values()

		std = list(student_data)
		response = {
				'msg':'Received successfully in py',
				'student_data':std,
				
			}
		return JsonResponse(response)

		
		# 	return JsonResponse("status",'Saved',safe=False)
		# else:
		# 	return JsonResponse("status",'Failed',safe=False)

def indexView(request):
	form = StudentForm()
	all_std = Student.objects.all()

	return render(request,'index.html',{'form':form,'student':all_std})