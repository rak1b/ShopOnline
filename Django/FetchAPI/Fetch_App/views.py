
from django.shortcuts import render
from django.http import JsonResponse


# index
def index(request):
    return render(request, 'index.html')


# ajax_posting function
def ajax_posting(request):
    if request.is_ajax():
        first_name = request.POST.get('first_name', None) # getting data from input first_name id
        last_name = request.POST.get('last_name', None)  # getting data from input last_name id
        print(first_name,last_name)
        if first_name and last_name: #cheking if first_name and last_name have value
            response = {
                         'msg':'Your form has been submitted successfully' # response message
            }
            return JsonResponse(response) # return response as JSON

def second(request):
	return render(request,'second.html')

# def second_ajax_posting(request):
# 	if request.is_ajax():
# 		fname = request.POST.get('firstname', None)
# first_name will be here
# 		lname = request.POST.get('lastname', None)
# 		print(fname,lname)
# 		if fname and lname:
# 			response = {
# 			# 'msg':f'{fname} {lname} submitted successfully'
# 			'msg':' submitted successfully'
# 			}
# 			return JsonResponse(response)

def second_ajax_posting(request):
    if request.is_ajax():
        fname = request.POST.get('first_name', None) # getting data from input first_name id
        lname = request.POST.get('last_name', None)  # getting data from input last_name id
        print(fname,lname)
        if fname and lname: #cheking if first_name and last_name have value
            response = {
                         'msg':'Your form has been submitted successfully' # response message
            }
            return JsonResponse(response)


def third(request):
	return render(request,'third.html')


def third_ajax(request):
	if request.is_ajax():
		name = request.POST.get('name')
		email = request.POST.get('email')
		password = request.POST.get('password')

		print(name,email,password)

		if name and email and password:
			response = {
				'msg':f'{name},Your Form submitted successfully'
			}
			return JsonResponse(response)