from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from.admin import FeedbackResource, BookingResource, ContactResource, View_roomResource


# Create your views here.

def index(request):
    return render(request, 'hotel_app/index.html')

@login_required(login_url='register')
def room(request):
	return render(request, 'hotel_app/rooms.html')

def about_us(request):
	return render(request, 'hotel_app/about-us.html')

@login_required(login_url='register')
def booking(request):
	return render(request, 'hotel_app/booking.html')

def booking_data(request):
	return render(request, 'hotel_app/booking_data.html')

def blog(request):
	return render(request, 'hotel_app/blog.html')

def contact(request):
	return render(request, 'hotel_app/contact.html')

@login_required(login_url='register')
def feedback(request):
	return render(request, 'hotel_app/feedback.html')

def register(request):
	return render(request, 'hotel_app/register.html')

def success_page(request):
	context = {}
	context['success'] = 'Thank you for contacting us, we will revert back to you shortly'
	return render(request, 'hotel_app/contact.html', context)

def feedback_success(request):
	context = {}
	context['success'] = 'Thank you for your feedback, it means alot to us'
	return render(request, 'hotel_app/feedback.html', context)

def booking_success(request):
	context = {}
	context['success'] = 'Booking was successful, thanks for choosing to stay with us !!!'
	return render(request, 'hotel_app/booking.html', context)

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
		user = request.user,
		name = request.POST['names'],
		email = request.POST['email'],
		room_type = request.POST['room_type'],
		feedback_type = request.POST['feedback_type'],
		service_type = request.POST['service_type'],
		room_number = request.POST['room_num'],
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

def view_room_form(request):
	context ={}
	view_room = View_room(
		Date_from = request.POST['date_from'],
		Date_to =  request.POST['date_to'],
		adult = request.POST['adult'],
		children = request.POST['children'],
		number_of_rooms = request.POST['no_rooms'],
		rooms = request.POST['available_room'],

		 )
	return view_room

def View_room_submit(request):
	context = {}
	if request.method == 'POST':
		View_room_model = view_room_form(request)

		View_room_model.save()
		return HttpResponseRedirect(reverse('rooms'))

	elif request.method == "GET":
		return render(request, 'hotel_app/index.html')

def user_reg_form(request):
	u = User(
		username = request.POST['username'],
		email = request.POST['email'],
		password = request.POST['password1']
		)
	return u

def user_registration(request):
	context = {}
	if request.method == 'POST':
		user_reg = user_reg_form(request)

		user_reg.save()
		return HttpResponseRedirect(reverse('register'))

	else:
		return render(request, 'hotel_app/register.html', context)

def login_process(request):
	context = {}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password1')

		print(username)

		print(password)

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('rooms'))
			else:
				return HttpResponseRedirect(reverse('register'))
		else:
			context['error'] = "Invalid Login credential, please kindly register if you dont have an account"
			return render(request, 'hotel_app/register.html', context)

	else:
		return render(request, 'hotel_app/register.html', context)

def logOut(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def BookingForm(request):
	b = Booking(
		user =request.user,
		name = request.POST['name'],
		check_in = request.POST['check_in'],
		check_out = request.POST['check_out'],
		no_of_days = request.POST['no_days'],
		no_of_adult = request.POST['no_adult'],
		room_type = request.POST['room_type'],
		email = request.POST['email'],
		phone_number = request.POST['tel'],
		address = request.POST['address'],
		price = request.POST['price'],

		)
	return b

def Booking_submit(request):
	if request.method == 'POST':
		booking_model = BookingForm(request)
		booking_model.save()

		return HttpResponseRedirect(reverse('bookingSuccessMessage'))

	else:
		return render(request, 'hotel_app/booking.html')

def export(request):
    person_resource = PersonResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response












