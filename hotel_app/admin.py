from django.contrib import admin

# Register your models here.
from hotel_app.models import Contact

admin.site.site_header = "Hotel Reservation Admin"
admin.site.index_title = "Hotel Reservation Admin"
admin.site.site_title = "Hotel Reservation Admin"


class ContactAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'subject', 'message']

admin.site.register(Contact, ContactAdmin)