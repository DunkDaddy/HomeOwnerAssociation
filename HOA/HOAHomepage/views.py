from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import requests
from HOAApi.models import *
# Create your views here.

def home(response):
    return render(response, "base.html")
