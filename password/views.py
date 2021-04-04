from django.shortcuts import render
from password_generator.choices import length_choices
import random
# Create your views here.

def index(request):
    context = {
        'length_choices' : length_choices,
    }

    return render(request,'index.html',context)


def about(request):
    return render(request,'about.html')

def make_password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('Numbers'):
        characters.extend(list('123456789'))

    if request.GET.get('special_numbers'):
        characters.extend(list('!@#$%^&*()<'))    

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQSTUVWXYZ'))

    length = int(request.GET.get('length',12))

    password = ''

    for num in range(length):
        password += random.choice(characters)

    context = {
        'password' : password
    } 
    return render(request,'password.html',context)  

