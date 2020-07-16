from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = ['name', 'mobile', 'subject', 'message']

		widgets = {
		'name' : forms.TextInput(attrs={'class': 'input form-control', 'placeholder': 'Your Name'}),
		'mobile' : forms.NumberInput(attrs={'class': 'input form-control', 'placeholder': 'Your Mobile'}),
		'subject' : forms.TextInput(attrs={'class': 'input form-control', 'placeholder': 'Subject'}),
		'message' : forms.Textarea(attrs={'class': 'textarea form-control', 'rows': 4, 'placeholder': 'Message'})
		}