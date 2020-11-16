from django import forms
from .models import Student_info

# class Student_info(forms.ModelForm):
#     class Meta:
#         model = Student_info
#         fields= ['name','email','passw']
#     



class myform(forms.Form):
	name = forms.CharField(label=False,
		widget=forms.TextInput(
			attrs={
			'placeholder':'Enter name:','class':'form-control'

			}

			))
	email = forms.EmailField(label=False,
		widget=forms.TextInput(
			attrs={
			'placeholder':'Enter Email:','class':'form-control'
			}

			))
	age = forms.CharField(label=False,
		widget=forms.TextInput(
			attrs={
			'placeholder':'Enter age:','class':'form-control'
			}

			))

	password = forms.CharField(label=False,
		widget=forms.PasswordInput(
			attrs={
			'placeholder':'Enter Password:','class':'form-control'
			}

			))
	

# class myform(forms.Form):
# 	name = forms.CharField(min_length=3,label='',initial='Rakib')
# 	email = forms.EmailField(help_text="Enter Name here")
# 	age = forms.CharField(label='',widget=forms.TextInput(attrs={
# 		'placeholder':'Enter Age:'

# 		}))
# 	password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
# 	address = forms.CharField()
