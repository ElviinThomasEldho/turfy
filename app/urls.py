from django.urls import path
from . import views

urlpatterns = [
    # User Views
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('search-turfs/', views.searchTurfs, name='searchTurfs'),
    path('view-turf/<int:pk>/', views.viewTurf, name='viewTurf'),
    path('create-booking/<int:pk>/', views.createBooking, name='createBooking'),
    path('complete-payment/<int:pk>/', views.completePayment, name='completePayment'),
    path('cancel-booking/<int:pk>/', views.cancelBooking, name='cancelBooking'),

    # Turf Views
    path('register-turf/', views.registerTurf, name='registerTurf'),
    path('view-turf-profile/', views.viewTurfProfile, name='viewTurfProfile'),
    path('edit-turf-profile/', views.editTurfProfile, name='editTurfProfile'),
    path('view-bookings/', views.viewBookings, name='viewBookings'),
    path('view-payment/<int:pk>/', views.viewPayment, name='viewPayment'),
    path('view-time-slots/', views.viewTimeSlots, name='viewTimeSlots'),
    path('add-time-slot/', views.addTimeSlot, name='addTimeSlot'),
    path('edit-time-slot/<int:pk>/', views.editTimeSlot, name='editTimeSlot'),
    path('delete-time-slot/<int:pk>/', views.deleteTimeSlot, name='deleteTimeSlot'),
]
