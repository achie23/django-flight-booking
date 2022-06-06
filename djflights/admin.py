from django.contrib import admin
from .models import (
    Airport, 
    Flight, 
    Passenger, 
    Service, 
    Package, 
    Contact
    )

# Register your models here.
class PassengerInline(admin.StackedInline):
    model = Passenger.flights.through
    extra = 1
    
class FlightAdmin(admin.ModelAdmin):
    inlines = [PassengerInline]
    
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
admin.site.register(Service)
admin.site.register(Package)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'name',)