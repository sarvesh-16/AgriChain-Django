from django.shortcuts import render
from django.http import HttpResponseBadRequest
import pyrebase
from django.contrib import auth as authe
from datetime import datetime
from django.shortcuts import redirect
from web3 import Web3
import json
from django.http import JsonResponse
import pyqrcode
from pyqrcode import QRCode


# Create your views here.

def home(request):
    return render(request,'main/index.html')

def about(request):
    return render(request,'main/about.html')    