from django import forms
from django.forms import ModelForm

from .models import Page

class PageForm(forms.ModelForm):
	class Meta:
		model = Page
		fields = ['language', 'city']

		lang_options = [
			('1', 'Python'),
			('2', 'Javascript'),
			('3', 'Java'),
			('4', 'C#'),
		]

		city_options = [
			('1', 'Киев'),
		]

		language = forms.ChoiceField(required=True, choices=lang_options)
		city = forms.ChoiceField(required=True, choices=city_options)
