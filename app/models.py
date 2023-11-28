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


class Payment(models.Model):

    player = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    turf = models.ForeignKey(Turf, null=True, on_delete=models.SET_NULL)
    
<<<<<<< HEAD
    
    mode





=======
>>>>>>> e43b5db55e9a5757540bde1b889852f5a45f92bc

class Turf(models.Model):
    TYPE =  (
        ('5s','5s'),
        ('7s','7s')
    )
<<<<<<< HEAD
=======

>>>>>>> e43b5db55e9a5757540bde1b889852f5a45f92bc
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    ownerName = models.CharField("First Name", max_length=25, null=True)
    turfName = models.CharField("Turf Name", max_length=25, null=True)
    location = models.CharField("Location ", max_length=200, null=True)
    phoneNumber = models.CharField("Phone Number", max_length=25, null=True)
    pricePerSlot = models.FloatField("Price Per Slot", max_length=3, null=True)
<<<<<<< HEAD
    fieldSize = models.CharField("fieldSize",max_length=3,choices=TYPE )
    
    
    def __str__(self):
        return str(self.id) + " | " + self.turfName + " | " + self.ownerName 
=======
    type = models.CharField("Type", max_length=25, choices=TYPE, null=True)
    
    slots = models.ManyToManyField(TimeSlot, null=True, blank=True)
    
    def __str__(self):
        return str(self.id) + " | " + self.turfName + " | " + self.ownerName 


>>>>>>> e43b5db55e9a5757540bde1b889852f5a45f92bc
