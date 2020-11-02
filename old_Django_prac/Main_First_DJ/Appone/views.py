from django.shortcuts import render,HttpResponse
# fron django.template import Template

# Create your views here.
def home(request):
    return render(request,'home.html')

def remove_punc(request):
	txt = request.POST.get('text_val','')
	puncuation = '''./?!,_=+-'''
	filtered_txt = ''
	for i in txt:
		if i not in puncuation:
			filtered_txt = filtered_txt + i
	dictt = {
			'original' : txt,
			'filtered': filtered_txt,
			}

	print(filtered_txt)		
	return render(request,'remove_punc.html',dictt)


def capitalize(request):
	txt = request.POST.get('text_cap_val','None')
	upper_txt = txt.upper()
	values = {
		'original' : txt,
		'filtered': upper_txt,
	}
	return render(request,'capitalize.html',values)
	
def ExtraSpaceRemove(request):
	txt = request.POST.get('extra_space_val','')
	filtered_txt = ''
	for i,j in enumerate(txt):
		if not (txt[i] == ' ' and txt[i+1]== ' '):
			filtered_txt = filtered_txt + j
	values = {
		'origin' : str(txt),
		'filtered': filtered_txt,
	}

	print(txt)
	return render(request,'ExtraSpaceRemove.html',values)
