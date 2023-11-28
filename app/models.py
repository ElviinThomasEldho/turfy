from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Player(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    firstName = models.CharField("First Name", max_length=25, null=True)
    lastName = models.CharField("Last Name", max_length=25, null=True)
    mobile = models.CharField("Mobile Number", max_length=25, null=True)
    email = models.EmailField("Email Address", null=True)
    dateOfBirth = models.DateField("Date of Birth", null=True)

    dateCreated = models.DateTimeField("Date Created", auto_created=True)
    # friends = models.ManyToManyField(self, blank=True,  null=True)

    def __str__(self):
        return str(self.id) + " | " + self.firstName + " " + self.lastName 
    
class Days(models.Model):
    days = models.CharField("Day of the week", max_length=25, null=True)
    
class TimeSlot(models.Model): 
    CHOICE = (
        ("AM","AM")
        ("PM","PM")
    )
    startTime = models.IntegerField("Start Time", max_length=2,null=True)
    choice = models.CharField("Choice",max_length=3,choices=CHOICE)
    endTime =models.IntegerField("End Time", max_length=2,null=True)
    choice = models.CharField("Choice",max_length=3,choices=CHOICE)
    days= models.ManyToManyField(Days, null=True, blank=True) 

class Turf(models.Model):
    TYPE =  (
        ('5s','5s'),
        ('7s','7s')
    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    ownerName = models.CharField("First Name", max_length=25, null=True)
    turfName = models.CharField("Turf Name", max_length=25, null=True)
    location = models.CharField("Location ", max_length=200, null=True)
    phoneNumber = models.CharField("Phone Number", max_length=25, null=True)
    pricePerSlot = models.FloatField("Price Per Slot", max_length=3, null=True)
    fieldSize = models.CharField("fieldSize",max_length=3,choices=TYPE )
    slots = models.ManyToManyField(TimeSlot, null=True, blank=True) 

    def __str__(self):
        return str(self.id) + " | " + self.turfName + " | " + self.ownerName 
    

class Booking(models.Model):
    player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)
    turf = models.ForeignKey(Turf, null=True, on_delete=models.SET_NULL)
    timeSlot = models.ForeignKey(TimeSlot, null=True, on_delete=models.SET_NULL)

    date = models.DateField("Date", null=True)
    noOfParticipants = models.IntegerField("No of Participants",max_length=2,null=True)



class Payment(models.Model):
    MODE =(
        ("UPI","UPI")
        ("Cash","Cash")
    )
    player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)
    turf = models.ForeignKey(Turf, null=True, on_delete=models.SET_NULL)
    booking = models.ForeignKey(Booking, null=True, on_delete=models.SET_NULL)

    mode = models.CharField("Payment Mode",max_length=3,choices=MODE)
    screenshot = models.ImageField("Payment Screenshot Upload",null=True)
    amount = models.FloatField("Toatl Amount ", max_length= 10, null = True)

