from django.shortcuts import render, HttpResponse
from home.models import Contacts
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "variable1":"This is sent",
        "var2":"OKAY!"
    }
    return render(request, "index.html", context)

def about(request):
    #return HttpResponse("this is my about page.")
    return render(request, "about.html")

def contacts(request):
    #return HttpResponse("this is my contacts page.")
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contacts = Contacts(name = name, email = email, desc = desc, date = datetime.today())
        contacts.save()
        messages.success(request, 'Your query saved successfully.')
    return render(request, "contacts.html")

def services(request):
    #return HttpResponse("this is my services page.")
    return render(request, "services.html")