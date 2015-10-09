from django import forms

import re

from .models import SignUp

class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		if domain != 'gmail':
			raise forms.ValidationError("please provide a gmail id")
		return email

	def clean_full_name(self):
		name = self.cleaned_data.get('full_name')

		if re.search(r"[0-9]", name):
			raise forms.ValidationError("please provide a valid name")
		elif not name:
			name = 'Anonymous'
		return name

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split(".")
		if domain != 'gmail':
			raise forms.ValidationError("please provide a gmail id")
		return email

	def clean_full_name(self):
		name = self.cleaned_data.get('full_name')

		if re.search(r"[0-9]", name):
			raise forms.ValidationError("please provide a valid name")
		return name
