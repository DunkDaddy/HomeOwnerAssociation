from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
import requests
from HOAApi.models import *
from .forms import RegistrerForm, LoginForm
# Create your views here.

def loginp(response):
    registrer = RegistrerForm
    login = LoginForm
    return render(response, "homepage.html", {"login": login, "registrer": registrer})
def home(response):
    loginpage = loginp(response)
    if response.method == "POST":
        x = ""
        registrer = RegistrerForm(response.POST)
        beboerListe = Beboer.objects.all()
        if registrer.is_valid():
            try:
                x = Beboer.objects.get(brugernavn=registrer.cleaned_data['brugernavn'])
                return loginpage
            except:
                beboer = Beboer(navn=registrer.cleaned_data['navn'], adresse=registrer.cleaned_data['adresse'], tlf=registrer.cleaned_data['tlf'], brugernavn=registrer.cleaned_data['brugernavn'], password=make_password(registrer.cleaned_data['password']), mail=registrer.cleaned_data['mail'])
                beboer.save()
                return render(response, 'success.html')
        login = LoginForm(response.POST)
        if login.is_valid():
            for person in beboerListe:
                if login.cleaned_data['brugernavn'] == person.brugernavn and check_password(login.cleaned_data['password'], person.password) == True:

                    andmeldelse = Andmeldelse.objects.all()
                    return render(response, 'success.html', {"Andmeldelser": andmeldelse, "person": person})

    if response.method == "GET":
        return loginpage
    else:
        return loginpage
