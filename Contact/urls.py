from django.urls import path
from  . import views
urlpatterns = [
    path('contact-us/',contact="contact_us"),
    path('comtact-store-contact/',views.store_contact,name="store_contact_us")
]
