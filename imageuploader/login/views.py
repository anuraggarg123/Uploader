from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
import pyautogui as pu
def login(request):
    if request.method == 'POST':
        person = request.POST['username']
        passwd = request.POST['encrypt']
        x = auth.authenticate(username=person, password=passwd) # username and password are names in database
        if x is None:
            pu.alert('Invalid Credentials')
            return render(request, 'login.html')
        else:
            auth.login(request, x)
            return redirect('/home1/')
    else:
        return render(request, 'login.html')