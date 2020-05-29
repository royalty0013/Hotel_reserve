from django.contrib import admin

# Register your models here.
from hotel_app.models import Contact, Feedback, Reservation

admin.site.site_header = "Blue-Jack Hotel Admin"
admin.site.index_title = "Blue-Jack Hotel Admin"
admin.site.site_title = "Blue-Jack Hotel Admin"


class ContactAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'subject', 'message']

admin.site.register(Contact, ContactAdmin)

class ReservationAdmin(admin.ModelAdmin):
	list_display = ["first_name","last_name","email","check_in","check_out","room_type" ]
	search_fields = ["first_name", "last_name"]

admin.site.register(Reservation, ReservationAdmin)

class FeedbackAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'room_type', 'feedback_type', 'service_type', 'feedback_description']

admin.site.register(Feedback, FeedbackAdmin)