from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
import os

# Create your views here.

def home(request):

	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data.get('name')
			mobile = form.cleaned_data.get('mobile')
			subject = form.cleaned_data.get('subject')
			message = form.cleaned_data.get('message')
			send_mail(
			    "Email from Senthil andavar | " + subject,
			    'Customer name : ' + name + '\n' + 'Customer Mobile : ' + mobile + '\n' + 'Message : '+ message,
			    os.environ.get('EMAIL_USER'),
			    [os.environ.get('EMAIL_TO_USER')],
			    fail_silently=False,
			)
			messages.success(request, f'   We have received your contact information. We will get back to you as soon as possible! Meanwhile, you can always reach us on +91 94866 47406 / +91 98427 47406')
			return redirect('home-page')
	else:	
		form = ContactForm()

	return render(request, 'index/home.html', {'form':form})


