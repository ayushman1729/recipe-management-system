from django.shortcuts import render, redirect
from django.http import HttpResponse
from vege.seed import *
from .utils import send_email_to_client, send_email_with_attachment
from django.conf import settings
import os
import random
from home.models import Car


def send_email(request):
    subject = "This email is from Django server with Attachment"
    message = "Hey please find this attach with this email"
    recipient_list = ["ayushman7310@gmail.com"]

    file_path = os.path.join(settings.BASE_DIR, "main.xlsx")

    send_email_with_attachment(subject, message, recipient_list, file_path)

    return redirect('/')
# def send_email(request):
#     send_email_to_client()
#     return redirect('/')

def home(request):
   #seed_db(100)

    Car.objects.create(car_name=f"Nexon={random.randint(0, 100)}")

    peoples=[
        {'name':'Abhijeet', 'age':26 },
        {'name':'Rohan Sharma', 'age':23},
        {'name':'Vicky Kaushal', 'age':24},
        {'name':'ayushman', 'age':21}
    ]
  
    for people in peoples:
       if people['age'] :
          print("Yes")
   
   #  vegetables=['Pumpkin', 'Tomato', 'Potatoe']

    return render(request,"home/index.html",
                   context={'page':'Django 2023 Tutorial',
                      'peoples':peoples
                            })

def test(request):
   return HttpResponse("test page")

def about(request):
  context={'page':'about'}
  return render(request,"home/about.html", context)   

def contact(request):
  context={'page': 'contact'}
  return render(request,"home/contact.html", context)   

def success(request):
    context={'page':'Contact'}
    return HttpResponse("<H1>Hey this is a Success page.</H1>")   

