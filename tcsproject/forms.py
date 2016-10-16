from django import forms
from models import Thesis
from django.forms import ModelForm

class AddThesisForm(forms.ModelForm):
	class Meta:
		model = Thesis
		fields = ['title',
				  'authors',
				  'emails',
				  'desc',
				  'abstract',
				  'no_of_pages',
				  'date_published',
				  'dept',
				  'category']

class ContactForm(forms.Form):
	name = forms.CharField(required=True)
	message = forms.CharField(max_length=500, widget=forms.Textarea, required=True)

class LikeForm(forms.Form):
	thesis = forms.CharField(max_length=500)
	like = forms.IntegerField()
	session_id = forms.CharField(max_length=500)

class SearchForm(forms.Form):
	thesis_title = forms.CharField(max_length=500)