from django import forms
from .import models

class CreateArticle(forms.ModelForm):
	class Meta:
		model = models.Page
		fields = ['title', 'body', 'slug', 'thumb']

