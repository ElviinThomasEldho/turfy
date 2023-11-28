from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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
                return redirect('createPlayer')

    context = {
        'form': form,
    }

    return render(request, 'app/register.html', context)

def createPlayer(request):

    context = {
        
    }

    return render(request, 'app/index.html', context)


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


def viewTurfs(request):

    context = {
        
    }

    return render(request, 'app/index.html', context)


def viewTurfDetails(request, pk):

    context = {
        
    }

    return render(request, 'app/index.html', context)


def createBooking(request, pk):

    context = {
        
    }

    return render(request, 'app/index.html', context)


def completePayment(request, pk):

    context = {
        
    }

    return render(request, 'app/index.html', context)


def cancelBooking(request, pk):

    context = {
        
    }

    return render(request, 'app/index.html', context)

#TURF VIEWS
def registerTurf(request):

    context = {
        
    }

    return render(request, 'app/index.html', context)


def viewTurfProfile(request):

    context = {
        
    }

    return render(request, 'app/index.html', context)


def editTurfProfile(request):

    context = {
        
    }

    return render(request, 'app/index.html', context)


def viewBookings(request):

    context = {
        
    }

    return render(request, 'app/index.html', context)


def viewPayment(request, pk):

    context = {
        
    }

    return render(request, 'app/index.html', context)


def viewTimeSlots(request):

    context = {
        
    }

    return render(request, 'app/index.html', context)


def addTimeSlot(request):

    context = {
        
    }

    return render(request, 'app/index.html', context)


def editTimeSlot(request, pk):

    context = {
        
    }

    return render(request, 'app/index.html', context)


def deleteTimeSlot(request, pk):

    context = {
        
    }

    return render(request, 'app/index.html', context)