from django.shortcuts import render
from myapp.models import Image
def show(request,id):
    g=Image.objects.get(pk=id)
    return render(request,'show.html',{'g':g})