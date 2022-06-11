# from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, 'about.html', {'gretting': 'Hello, bro!'})

def reversed(request):
    user_text = request.GET['textarea']
    return render(request, 'reversed.html', {'u_text': user_text[::-1]})

def home(request):
    return render(request, 'home.html')

# def home(request):
#     return HttpResponse('This is my home')