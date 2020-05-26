from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

def index(request):
    return render(request, 'hotel_app/index.html')

def room(request):
	return render(request, 'hotel_app/rooms.html')

def about_us(request):
	return render(request, 'hotel_app/about-us.html')

def blog(request):
	return render(request, 'hotel_app/blog.html')

def contact(request):
	return render(request, 'hotel_app/contact.html')

def success_page(request):
	context = {}
	context['success'] = 'Thank you for contacting us, we will revert back to you shortly'
	return render(request, 'hotel_app/contact.html', context)

def contact_form(request):
	f = Contact(
		name = request.POST['names'],
		email = request.POST['email'],
		subject = request.POST['subject'],
		message = request.POST['message'],

		)
	return f

def contact_submit(request):
	context = {}
	if request.method == 'POST':
		contact_model = contact_form(request)

		contact_model.save()

		return HttpResponseRedirect(reverse('successMessage'))

	elif request.method == 'GET':
		return render(request, 'hotel_app/contact.html')


