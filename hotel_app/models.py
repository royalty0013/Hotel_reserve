from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	subject = models.CharField(max_length=100)
	message = models.TextField(max_length=500, null=True, blank=True)

	class meta:
		verbose_name = "Contact"
		verbose_name_plural = "Contact"

	def __str__(self):
		return self.name

class Reservation(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	check_in = models.DateField()
	check_out = models.DateField() 
	room_type = models.CharField(max_length=100)

	class meta: 
		verbose_name = "Reservation"
		verbose_plural_name = "Reservation"

	def __str__(self):
		return self.first_name + " " + self.last_name

class Feedback(models.Model):
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

	class meta:
		verbose_name = "Feedback"
		verbose_name_plural = "Feedbacks"

		def __str__(self):
			return self.name