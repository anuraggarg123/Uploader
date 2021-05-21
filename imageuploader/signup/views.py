from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
import pyautogui as p

def signup(request):
    if (request.method == 'POST'):
        user = request.POST['username']
        last = request.POST['last_name']
        Email = request.POST['e_mail']
        passwd = request.POST['pass_word']
        if User.objects.filter(username=user).exists():
            p.alert('User exists.Please write different user')
            return render(request, 'signup.html')
        else:
            user = User.objects.create_user(username=user, last_name=last, email=Email,
                                            password=passwd)   # creating object in User table(inbuilt)
            user.save()
            p.confirm('User has created')
            return redirect('/')      # It returns to home page('/' symbol)
    else:
        return render(request, 'signup.html')
