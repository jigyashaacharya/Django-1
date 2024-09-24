from django.http import HttpResponse
from django.shortcuts import render

def landingpage(request):
    return render(request,"home.html")
    return HttpResponse(html)

def About(request):
    return render(request,"about.html")
    return HttpResponse(html)

def Product(request):
    return render(request,"product.html")
    return HttpResponse(html)

def Categories(request):
    return render(request,"categories.html")
    return HttpResponse(html)

def Contact(request):
    return render(request,"contact.html")
    return HttpResponse(html)



 




 