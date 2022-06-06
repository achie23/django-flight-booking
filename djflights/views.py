from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import (
    Flight, 
    Passenger,
    Service,
    Package,
    )

from django.contrib import messages
from django.views import generic
from .forms import ContactForm

# Create your views here.
def index(request):
    context = {
        "flights": Flight.objects.all(),
        "packages": Package.objects.all(),
        "services": Service.objects.all(),
    }
    return render(request, "djflights/index.html", context)

def flights(request):
    context = {
        "flights": Flight.objects.all(),
    }
    return render(request, "djflights/flights.html", context)

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight Does Not Exist")
    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    }
    return render(request, "djflights/flight.html", context)

def book(request, flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=passenger_id)
    except KeyError:
        return render(request, "djflights/error.html", {"message": "No flight selected."})
    except Flight.DoesNotExist:
        return render(request, "djflights/error.html", {"message": "No such flight."})
    except Passenger.DoesNotExist:
        return render(request, "djflights/error.html", {"message": "No passenger."})
    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

def packages(request):
    context = {
        "packages": Package.objects.all(),
    }
    return render(request, "djflights/package-detail.html", context)

class ContactView(generic.FormView):
    template_name = "djflights/contact.html"
    form_class = ContactForm
    success_url = "/"
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. We will be in touch soon.')
        return super().form_valid(form)