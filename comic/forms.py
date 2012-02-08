from django import forms

class AddComic(forms.Form):
	name = forms.CharField(max_length=100)
	comic = forms.ImageField()
	description = forms.CharField(required=False,widget=forms.Textarea)
	