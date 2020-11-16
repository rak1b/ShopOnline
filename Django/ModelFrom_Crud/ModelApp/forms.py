from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model=Student
		fields = ['st_name','st_email','st_pass']
		labels = {
			'st_name':'',
			'st_email':'',
			'st_pass':'',

		}
		widgets = {
			'st_name':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':"name",
				}),

			'st_email':forms.EmailInput(attrs={
				'class':'form-control',
				'placeholder':"Email",

				}),

			'st_pass':forms.PasswordInput(attrs={
				'placeholder':"Password",
				'class':'form-control',
				})

		}
