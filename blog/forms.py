from django import forms
from .models import Post

class PostForm(forms.ModelForm): # PostForm is the name of the form.

	class Meta:
		model = Post
		fields = ('title', 'text',)