from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from .models import Contact

# Create your views here.

def view_home(request):
    return render(request, 'portal/home.html')

def about_view(request):
    return render(request, 'portal/about.html')

def neet_view(request):
    return render(request, 'portal/neet.html')

def selassor_view(request):
    return render(request, 'portal/selassor.html')

def fmcg_view(request):
    return render(request, 'portal/fmcg.html')


def pricing_view(request):
    return render(request, 'portal/pricing.html')

def login_view(request):
    return HttpResponseRedirect('http://app.gemsnext.com')

def contact_view(request):
    if request.method=="POST":
        contact=Contact()
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        quesrion=request.POST.get('question')
        contact.first_name=first_name
        contact.last_nam=last_name
        contact.email=email
        contact.phone_number=phone_number
        contact.question=quesrion
        contact.save()
        return render(request,'portal/conthanx.html')
    return render(request, 'portal/contact.html')
from django.shortcuts import render


