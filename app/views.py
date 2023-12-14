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
                return redirect('chooseUser')

    context = {
        'form': form,
    }

    return render(request, 'app/register.html', context)


def chooseUser(request):
    context = {
    }

    return render(request, 'app/chooseUser.html', context)

def registerPlayer(request):
    user = request.user
    form = PlayerForm()

    if (Player.objects.filter(user=user).exists()):
            return redirect('playerProfile')
    else:
        if request.method == 'POST':
            form = PlayerForm(request.POST, request.FILES)
            if form.is_valid():
                player = form.save()
                player.user = user
                player.firstName = user.first_name
                player.lastName = user.last_name
                player.emailID = user.email
                player.save()

                add_group = Group.objects.get(name='Player')
                add_group.user_set.add(request.user)
                return redirect('playerProfile')

        context = {
            'form': form,
        }

        return render(request, 'app/registerPlayer.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('chooseUser')

        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'app/login.html')


def playerProfile(request):
    player = Player.objects.get(user=request.user)

    context = {
        'player':player,
    }

    return render(request, 'app/playerProfile.html', context)


def searchTurfs(request):
    turfs = Turf.objects.all()

    context = {
        'turfs':turfs,
    }

    return render(request, 'app/searchTurf.html', context)


def viewTurf(request, pk):
    turf = Turf.objects.get(id = pk)

    context = {
        'turf':turf,        
    }

    return render(request, 'app/viewTurf.html', context)


def createBooking(request, pk):
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('completePayment')

    context = {
        'form': form,
    }

    return render(request, 'app/bookTurf.html', context)


def completePayment(request, pk):
    form = PaymentForm()

    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('playerProfile')

    context = {
        'form': form,
    }

    return render(request, 'app/completePayment.html', context)


def cancelBooking(request, pk):
    booking = Booking.objects.get(id=pk)
    booking.delete()
    redirect('playerProfile')

#TURF VIEWS
def registerTurf(request):
    user = request.user
    form = TurfForm(initial={'user': request.user.id})

    if (Turf.objects.filter(user=user).exists()):
            return redirect('turfProfile')
    else:
        if request.method == 'POST':
            form = TurfForm(request.POST, request.FILES)
            if form.is_valid():
                turf = form.save()
                turf.user = request.user
                turf.save()
                add_group = Group.objects.get(name='Turf')
                add_group.user_set.add(request.user)
                return redirect('turfProfile')

        context = {
            'form': form,
        }

        return render(request, 'app/registerTurf.html', context)


def turfProfile(request):
    turf = Turf.objects.get(user=request.user)
    bookings = Booking.objects.filter(turf=turf)
    payments = Payment.objects.filter(turf=turf)
    slots = turf.slots

    context = {
        'turf':turf,
        'bookings':bookings,
        'payments':payments,
        'slots':slots,
    }

    return render(request, 'app/turfProfile.html', context)


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

    return render(request, 'app/editTurfProfile.html', context)


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