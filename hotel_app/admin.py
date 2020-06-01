from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from import_export import resources

# Register your models here.
from hotel_app.models import Contact, Feedback, View_room, Booking

admin.site.site_header = "Blue-Jack Hotel Admin"
admin.site.index_title = "Blue-Jack Hotel Admin"
admin.site.site_title = "Blue-Jack Hotel Admin"


class FeedbackResource(resources.ModelResource):
    class Meta:
        model = Feedback

class BookingResource(resources.ModelResource):
    class Meta:
        model = Booking

class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact

class View_roomResource(resources.ModelResource):
    class Meta:
        model = View_room

FeedbackResource = FeedbackResource()
dataset = FeedbackResource.export()
dataset.csv

BookingResource = BookingResource()
dataset = BookingResource.export()
dataset.csv

ContactResource = ContactResource()
dataset = ContactResource.export()
dataset.csv

View_roomResource = View_roomResource()
dataset = View_roomResource.export()
dataset.csv

class ContactAdmin(ImportExportModelAdmin):
	list_display = ['name', 'email', 'subject', 'message', 'added']

admin.site.register(Contact, ContactAdmin)

class FeedbackAdmin(ImportExportModelAdmin):
	list_display = ['user', 'name', 'email', 'room_type', 'feedback_type', 'service_type', 'feedback_description', 'added']

admin.site.register(Feedback, FeedbackAdmin)

class View_roomAdmin(ImportExportModelAdmin):
	list_display = ['Date_from', 'Date_to', 'adult', 'children', 'number_of_rooms', 'rooms', 'time']

admin.site.register(View_room, View_roomAdmin)

class BookingAdmin(ImportExportModelAdmin):
	list_display = ['user', 'name', 'check_in', 'check_out', 'no_of_days', 'no_of_adult', 'room_type', 'email', 'phone_number', 'price', 'address', 'added']

admin.site.register(Booking, BookingAdmin)

