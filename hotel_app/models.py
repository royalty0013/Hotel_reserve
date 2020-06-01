from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	subject = models.CharField(max_length=100)
	message = models.TextField(max_length=500, null=True, blank=True)
	added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, null=True, blank=True)

	class meta:
		verbose_name = "Contact"
		verbose_name_plural = "Contact"

	def __str__(self):
		return self.name

class Feedback(models.Model):
	user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	name = models.CharField(max_length=100)
	email = models.EmailField()

	ROOM_TYPE = (
	('Twin Room With Seaview', 'Twin Room With Seaview'),
	('Deluxe Suite', 'Deluxe Suite'),
	('Double Room', 'Double Room'),
	('Single Room', 'Single Room'),
		)

	room_type = models.CharField(max_length=100, choices=ROOM_TYPE, null=True)

	FEEDBACK_TYPE = (
	('Compliment', 'Compliment'),
	('Complaint', 'Complaint'),
	('Both', 'Both'),
	)
	feedback_type = models.CharField(max_length=100, choices=FEEDBACK_TYPE, null=True)

	SERVICE_TYPE = (
	('Food', 'Food'),
	('Room', 'Room'),
	('Spa', 'Spa'),
	('Others', 'Others'),

	)
	service_type = models.CharField(max_length=100, choices=SERVICE_TYPE, null=True)
	room_number = models.CharField(max_length=50, default=0)
	feedback_description = models.TextField(max_length=200)
	added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	updated = models.DateTimeField(auto_now=True, null=True, blank=True)

	class meta:
		verbose_name = "Feedback"
		verbose_name_plural = "Feedbacks"

		def __str__(self):
			return self.name

class View_room(models.Model):
	Date_from = models.CharField(max_length=50)
	Date_to = models.CharField(max_length=50)
	adult = models.IntegerField(default=0)
	children = models.IntegerField(default=0)
	number_of_rooms = models.IntegerField(default=0)
	rooms = models.CharField(max_length=50)
	time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	class meta:
		verbose_name = "View room"
		verbose_name_plural = " View rooms"

	

class Booking(models.Model):
	user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	name = models.CharField(max_length=50)
	check_in = models.CharField(max_length=50)
	check_out = models.CharField(max_length=50)
	no_of_days = models.IntegerField()

	ADULT = [
	("1", "1"),
	("2", "2"),
	("3", "3"),

	]
	no_of_adult = models.CharField(max_length=20, choices=ADULT)

	ROOM_TYPE = [
	("Deluxe Suite", "Deluxe Suite"),
	("Twin Room With Seaview", "Twin Room With Seaview"),
	("Double Room", "Double Room"),
	("Single Room", "Single Room"),

	]

	room_type = models.CharField(max_length=50)
	email = models.EmailField()
	phone_number = models.CharField(max_length=50)
	price = models.IntegerField()
	address = models.CharField(max_length=50, null=True, blank=True)
	added = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	class Meta:
		verbose_name = "Booking"
		verbose_name_plural = "Bookings"

	def __str__(self):
		return self.name



