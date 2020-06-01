from django.urls import path
from hotel_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.room, name='rooms'),
    path('about_us/', views.about_us, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
    path('booking_data/', views.booking_data, name='booking_data'),
    path('register/', views.register, name='register'),
    path('success/', views.success_page, name='successMessage'),
    path('contact_submit/', views.contact_submit, name='contact_submit'),
    path('feedback_success/', views.feedback_success, name='feedbackSuccessMessage'),
    path('feedback_submit/', views.feedback_submit, name='feedback_submit'),
    path('view_room_submit/', views.View_room_submit, name='view_room_submit'),
    path('user_registration/', views.user_registration, name='user_registration'),
    path('login_process/', views.login_process, name='login_process'),
    path('logout/', views.logOut, name='logout'),
    path('booking/', views.booking, name='booking'),
    path('submit_booking/', views.Booking_submit, name='submit_booking'),
    path('booking_success/', views.booking_success, name='bookingSuccessMessage'),

]