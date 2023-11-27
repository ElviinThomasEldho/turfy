from django.shortcuts import render

# Create your views here.

# USER VIEWS
def index(request):

    context = {

    }

    return render(request, 'app/index.html', context)


def register(request):

    context = {
        
    }

    return render(request, 'app/index.html', context)


def login(request):

    context = {
        
    }

    return render(request, 'app/index.html', context)


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