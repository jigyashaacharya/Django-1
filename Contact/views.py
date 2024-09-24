from django.shortcuts import render,redirect
from django import Httpresponse
from django.contrib import messages
from .models import contact
 
 
def contact(request):
    return render(request,"contact.html")
     
    
def store_contact (request):
    # try:
    #     email = request.POST['email']
    # except:
    #     return Httpresponse("Error")
    # message = request.POST('message')
    # return Httpresponse(f'congrats! message is sent  to {email},{message}')
    form_email =request.POST['email']
    form_message  = request.POST['message']
    
    contact.objects.create(email=form_email, message =form_message)
    
    messages.success(request, 'Your message saved successfully')
    return redirect("contact_us")





    