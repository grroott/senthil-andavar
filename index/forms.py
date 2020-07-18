from django import forms
from .models import Contact, Newsletter

class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = ['name', 'mobile', 'subject', 'message']

		widgets = {
		'name' : forms.TextInput(attrs={'class': 'input form-control', 'placeholder': 'Your Name'}),
		'mobile' : forms.TextInput(attrs={'class': 'input form-control', 'placeholder': 'Your Mobile'}),
		'subject' : forms.TextInput(attrs={'class': 'input form-control', 'placeholder': 'Subject'}),
		'message' : forms.Textarea(attrs={'class': 'textarea form-control', 'rows': 4, 'placeholder': 'Message'})
		}

class NewsletterForm(forms.ModelForm):
	class Meta:
		model = Newsletter
		fields = ['email']

		widgets = {
		'email' : forms.EmailInput(attrs={'class': 'input form-control', 'placeholder': 'Your Email', 'style': 'width:300px'})
		}