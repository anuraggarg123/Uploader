from django.shortcuts import render,redirect
from myapp.models import Image
def delete(request,id):
    p=Image.objects.get(pk=id)
    p.delete()
    return redirect('/home1')
