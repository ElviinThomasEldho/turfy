from django.urls import path
from . import views

urlpatterns = [
    # User Views
    path('', views.index, name='index'),
    path('login/', views.loginUser, name='loginUser'),
    path('logout/', views.logoutUser, name='logoutUser'),
    
    path('register/', views.register, name='register'),
    path('register-player/', views.registerPlayer, name='registerPlayer'),
    path('player-profile/', views.playerProfile, name='playerProfile'),
    path('search-turfs/', views.searchTurfs, name='searchTurfs'),
    path('view-turf/<int:pk>/', views.viewTurf, name='viewTurf'),
    # path('create-booking/<int:pk>/', views.createBooking, name='createBooking'),
    path('complete-payment/<int:pk>/', views.completePayment, name='completePayment'),
    path('cancel-booking/<int:pk>/', views.cancelBooking, name='cancelBooking'),

    # Turf Views
    path('register-turf/', views.registerTurf, name='registerTurf'),
    path('turf-profile/', views.turfProfile, name='turfProfile'),
    path('edit-turf-profile/', views.editTurfProfile, name='editTurfProfile'),
    path('add-time-slot/', views.addTimeSlot, name='addTimeSlot'),
    path('edit-time-slot/<int:pk>/', views.editTimeSlot, name='editTimeSlot'),
    path('delete-time-slot/<int:pk>/', views.deleteTimeSlot, name='deleteTimeSlot'),
]
