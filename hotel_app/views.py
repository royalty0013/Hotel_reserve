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

def feedback(request):
	return render(request, 'hotel_app/feedback.html')

def success_page(request):
	context = {}
	context['success'] = 'Thank you for contacting us, we will revert back to you shortly'
	return render(request, 'hotel_app/contact.html', context)

def feedback_success(request):
	context = {}
	context['success'] = 'Thank you for your feedback, it means alot to us'
	return render(request, 'hotel_app/feedback.html', context)

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

def feedback_form(request):
	F_type = Feedback(
		name = request.POST['names'],
		email = request.POST['email'],
		room_type = request.POST['room_type'],
		feedback_type = request.POST['feedback_type'],
		service_type = request.POST['service_type'],
		room_number = request.POST['room_number'],
		feedback_description = request.POST['feedback_desc']
		)

	return F_type


def feedback_submit(request):
	context = {}
	if request.method == 'POST':
		feedback_model = feedback_form(request)

		feedback_model.save()
		return HttpResponseRedirect(reverse('feedbackSuccessMessage'))

	elif request.method == "GET":
		return render(request, 'hotel_app/feedback.html')


