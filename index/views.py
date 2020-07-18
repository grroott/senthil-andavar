from django.shortcuts import render
from .models import Contact
from .forms import ContactForm, NewsletterForm
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
import os

# Create your views here.

def home(request):

	if request.method == "POST":
		if request.POST.get("message_form") == 'message_form':
			message_form = ContactForm(request.POST)
			if message_form.is_valid():
				message_form.save()
				name = message_form.cleaned_data.get('name')
				mobile = message_form.cleaned_data.get('mobile')
				subject = message_form.cleaned_data.get('subject')
				message = message_form.cleaned_data.get('message')
				send_mail(
				    "Email from Senthil andavar | " + subject,
				    'Customer name : ' + name + '\n' + 'Customer Mobile : ' + mobile + '\n' + 'Message : '+ message,
				    os.environ.get('EMAIL_USER'),
				    [os.environ.get('EMAIL_TO_USER')],
				    fail_silently=False,
				)
				messages.success(request, f'   We have received your contact information. We will get back to you as soon as possible! Meanwhile, you can always reach us on +91 94866 47406 / +91 98427 47406')
				return redirect('home-page')
		elif request.POST.get("email_form") == 'email_form':
			print("hello")
			email_form = NewsletterForm(request.POST)
			if email_form.is_valid():
				email_form.save()
				email = email_form.cleaned_data.get('email')
				send_mail(
				    "Email from Senthil andavar | New subscriber for NewsLetter",
				    'Customer email : ' + email,
				    os.environ.get('EMAIL_USER'),
				    [os.environ.get('EMAIL_TO_USER')],
				    fail_silently=False,
				)
				messages.success(request, f"   Thanks for subscribing for our NewsLetter! We don't spam your mailbox. Stay tuned! Meanwhile, you can always reach us on +91 94866 47406 / +91 98427 47406")
				return redirect('home-page')

	else:	
		message_form = ContactForm() 
		email_form =  NewsletterForm()

	context = {
	'message_form':message_form,
	'email_form': email_form
	}

	return render(request, 'index/home.html', context)


