from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from . import templates


likes = 0


def home(request):
    if request.user.is_authenticated:
        return HttpResponse('<h1>Hello world</h1>')
    else: return redirect('auth')


def stav_like(request):
    return render(request, 'likes.html')


def like(request):
    global likes
    if request.method == 'POST':
        likes += 1
        return JsonResponse({'likes' : likes})
    else:
        return JsonResponse({'error' : 'Invalid request method'})


def authenticate_user(request):
    if request.method == 'POST':

        data = request.POST
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)
        return redirect('home')

    else: return render(request, 'register.html')

# Create your views here.
def check_username(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        user_exists = User.objects.filter(username=username).exists()
        return JsonResponse({'result' : user_exists})
    return JsonResponse({'error':'Only GET method'}, status=405)