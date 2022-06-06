from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    
    def __str__(self):
        return f"{self.id} - {self.origin} to {self.destination}"
    
class Passenger(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="service")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="package")
    is_active = models.BooleanField(default=True)
            
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    
    def __str__(self):
        return f'{self.name}'