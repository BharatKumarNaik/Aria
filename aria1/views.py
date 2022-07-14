from django.shortcuts import render
from django.http import HttpResponse
from aria1.models import Contact
from datetime import datetime


# Create your views here.

def home(request):
    # return HttpResponse("working")
    return render(request,'home.html')

def music(request):
    return render(request,'music.html')

def videos(request):
    return render(request,'videos.html')

def playlist(request):
    return render(request,'playlist.html')

def settings(request):
    return render(request,'settings.html')

def contact(request):
    if request.method == "POST":
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        text = request.POST.get('text')
        contact = Contact(email=email,phone=phone,text=text,date=datetime.today())
        contact.save()
    return render(request,'contact.html')
