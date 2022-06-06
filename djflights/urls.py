from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

# app_name = "djflights"

urlpatterns = [
    path("", views.index, name="index"),
    path("flights", views.flights, name="flights"),
    path("<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/book", views.book, name="book"),
    path("packages", views.packages, name="packages"),
    path("contact", views.ContactView.as_view(), name="contact"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
