from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User

from .models import *
from .forms import *

# Create your views here.

# USER VIEWS
def index(request):

    context = {

    }

    return render(request, 'app/index.html', context)


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')

    context = {
        'form': form,
    }

    return render(request, 'app/register.html', context)

def createPlayer(request):
    user = request.user
    form = PlayerForm(initial={'user': request.user.id})

    if (Player.objects.filter(user=user).exists()):
            return redirect('profile')
    else:
        if request.method == 'POST':
            form = PlayerForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

                player = Player.objects.get(user=request.user)
                player.firstName = user.first_name
                player.lastName = user.last_name
                player.emailID = user.email
                player.save()

                add_group = Group.objects.get(name='player')
                add_group.user_set.add(request.user)
                return redirect('profile')

        context = {
            'form': form,
        }

        return render(request, 'app/createPlayer.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'app/login.html')


def searchTurfs(request):
    turfs = Turf.objects.all()

    context = {
        'turfs':turfs,
    }

    return render(request, 'app/index.html', context)


def viewTurf(request, pk):
    turf = Turf.objects.get(id = pk)

    context = {
        'turf':turf,        
    }

    return render(request, 'app/index.html', context)


def createBooking(request, pk):
    form = BookingForm(initial={'user': request.user.id})

    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('completePayment')

    context = {
        'form': form,
    }

    return render(request, 'app/createBooking.html', context)


def completePayment(request, pk):
    form = PaymentForm(initial={'user': request.user.id})

    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {
        'form': form,
    }

    return render(request, 'app/completePayment.html', context)


def cancelBooking(request, pk):
    booking = Booking.objects.get(id=pk)
    booking.delete()
    redirect('profile')

#TURF VIEWS
def registerTurf(request):
    user = request.user
    form = TurfForm(initial={'user': request.user.id})

    if (Turf.objects.filter(user=user).exists()):
            return redirect('profile')
    else:
        if request.method == 'POST':
            form = TurfForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                add_group = Group.objects.get(name='turf')
                add_group.user_set.add(request.user)
                return redirect('viewTurfProfile')

        context = {
            'form': form,
        }

        return render(request, 'app/registerTurf.html', context)


def viewTurfProfile(request):
    turf = Turf.objects.get(user=request.user)

    context = {
        'turf':turf,
    }

    return render(request, 'app/viewTurfProfile.html', context)


def editTurfProfile(request):
    user = request.user
    turf = Turf.objects.get(user=user)
    form = TurfForm(instance=turf)

    if request.method == 'POST':
        form = TurfForm(request.POST, request.FILES, instance=turf)
        if form.is_valid():
            form.save()
            return redirect('viewTurfProfile')

    context = {
        'turf': turf,
        'form': form,
    }

    return render(request, 'trainee/edit.html', context)


def viewBookings(request):
    turf = Turf.objects.get
    bookings = Booking.objects.filter(turf)

    context = {
        "turf":turf,    
        "bookings":bookings,          
    }

    return render(request, 'app/index.html', context)


def viewPayment(request, pk):
    turf = Turf.objects.get(user=request.user)
    payment = Payment.objects.get(id=pk)

    context = {
        "turf":turf,
        "payment":payment,
    }

    return render(request, 'app/index.html', context)


def viewTimeSlots(request):
    turf = Turf.objects.get(user=request.user)
    slots = TimeSlot.objects.filter(turf=turf)

    context = {
        "turf":turf,
        "slots":slots,        
    }

    return render(request, 'app/index.html', context)


def addTimeSlot(request):
    turf = Turf.objects.get(user=request.user)
    form = TimeSlotForm(initial={'turf': turf})

    if request.method == 'POST':
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            form.save()
            add_group = Group.objects.get(name='turf')
            add_group.user_set.add(request.user)
            return redirect('viewTurfProfile')

    context = {
        'form': form,
    }

    return render(request, 'app/registerTurf.html', context)


def editTimeSlot(request, pk):

    context = {
        
    }

    return render(request, 'app/index.html', context)


def deleteTimeSlot(request, pk):

    context = {
        
    }

    return render(request, 'app/index.html', context)