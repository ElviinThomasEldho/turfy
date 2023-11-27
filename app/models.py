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
    
class Turf(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    ownerName = models.CharField("First Name", max_length=25, null=True)
    turfName = models.CharField("Turf Name", max_length=25, null=True)
    location = models.CharField("Location ", max_length=200, null=True)
    phoneNumber = models.CharField("Phone Number", max_length=25, null=True)
    pricePerSlot = models.FloatField("Price Per Slot", max_length=3, null=True)
    TYPE =  (
        ('5s',''),
        ('7s','female')
    )
    
    def __str__(self):
        return str(self.id) + " | " + self.turfName + " | " + self.ownerName 