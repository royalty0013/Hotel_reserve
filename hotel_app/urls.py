from django.urls import path
from hotel_app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.room, name='rooms'),
    path('about_us/', views.about_us, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success_page, name='successMessage'),
    path('contact_submit/', views.contact_submit, name='contact_submit'),

]