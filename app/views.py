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

    return render(request, 'app/chooseUser.html')


def registerPlayer(request):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.create_user(username=data.get('username'),email=data.get('email'),password=data.get('password1'))
        login(request, user)
        
        player = Player.objects.create(user=user, firstName=data.get('first_name'), lastName=data.get('last_name'), mobile=data.get('mobile'), email=data.get('email'), dateOfBirth=data.get('dateOfBirth'))
        print(player)
        
        add_group = Group.objects.get(name='Player')
        add_group.user_set.add(request.user)
        return redirect('playerProfile')

    context = {
        # 'form': form,
    }

    return render(request, 'app/registerPlayer.html', context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print(user, request.user.groups, request.user.groups.exists())
            if request.user.groups.exists(): 
                groups = set(group.name for group in request.user.groups.all())
                for group in groups:
                    print(group)
                    if group == "Turf":
                        return redirect('turfProfile')
                    elif group == "Player":
                        return redirect('playerProfile')
            else:
                return redirect('chooseUser')

        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'app/login.html')


def logoutUser(request):
    logout(request)
    return redirect('loginUser')


def playerProfile(request):
    player = Player.objects.get(user=request.user)
    bookings = Booking.objects.filter(player=player)

    context = {
        'player':player,
        'bookings':bookings,
    }

    return render(request, 'app/playerProfile.html', context)


def searchTurfs(request):
    turfs = Turf.objects.all()

    context = {
        'turfs':turfs,
    }

    return render(request, 'app/searchTurf.html', context)


def viewTurf(request, pk):
    player = Player.objects.get(user = request.user)
    turf = Turf.objects.get(id=pk)
    slots = turf.slots.all()
    
    if request.method == 'POST':
        data = request.POST
        print(data)
        slot = TimeSlot.objects.get(id=request.POST["slot"])
        booking = Booking.objects.create(player=player, turf=turf, timeSlot = slot, date = request.POST["date"])
        return redirect('/complete-payment/'+str(booking.id)+'/')

    context = {
        'slots':slots,        
    }

    return render(request, 'app/viewTurf.html', context)


def createBooking(request, pk):
    form = BookingForm()
    player = Player.objects.get(user = request.user)
    turf = Turf.objects.get(id=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            booking = form.save()
            booking.player = player
            booking.turf = turf
            booking.save()
            return redirect('/complete-payment/'+str(booking.id)+'/')

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
    if request.method == 'POST':
        data = request.POST
        user = User.objects.create_user(username=data.get('username'),email=data.get('email'),password=data.get('password1'))
        login(request, user)
        
        turf = Turf.objects.create(user=user, turfName=data.get('turfName'), location=data.get('location'), phoneNumber=data.get('phoneNumber'), pricePerSlot=data.get('pricePerSlot'), fieldSize=data.get('fieldSize'))
        print(turf)
        
        add_group = Group.objects.get(name='Turf')
        add_group.user_set.add(request.user)
        return redirect('turfProfile')

    context = {
    }

    return render(request, 'app/registerTurf.html', context)


def turfProfile(request):
    turf = Turf.objects.get(user=request.user)
    bookings = Booking.objects.filter(turf=turf)
    payments = Payment.objects.filter(turf=turf)
    slots = turf.slots.all()

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
            return redirect('turfProfile')

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
            slot = form.save()
            turf.slots.add(slot)
            return redirect('turfProfile')

    context = {
        'form': form,
    }

    return render(request, 'app/addTimeSlots.html', context)


def editTimeSlot(request, pk):
    turf = Turf.objects.get(user=request.user)
    timeSlot = TimeSlot.objects.get(id=pk)
    form = TimeSlotForm(instance=timeSlot)

    if request.method == 'POST':
        form = TimeSlotForm(request.POST, instance=timeSlot)
        if form.is_valid():
            slot = form.save()
            turf.slots.add(slot)
            return redirect('turfProfile')

    context = {
        'form': form,
    }

    return render(request, 'app/editTimeSlots.html', context)


def deleteTimeSlot(request, pk):

    context = {
        
    }

    return render(request, 'app/index.html', context)