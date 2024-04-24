import requests
from django.shortcuts import render, redirect
from logs.models import Log
from django.db import transaction

def __get_courses():
    url = 'http://localhost:8001/api/v1/courses/'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    
    return []

def __update_course(pk):
    url = f'http://localhost:8001/api/v1/courses/{pk}/publish'
    payload = {
        'published_by': 1
    }
    response = requests.put(url, data=payload)
    
    if response.status_code == 200:
        return response.json()
    
    raise Exception('Failed to update course')

def home(request):
    courses = __get_courses()
    return render(request, 'home.html', {
        'courses': courses
    })

def update_course(request, pk):
    try:
        with transaction.atomic():
            Log.objects.create(message='Nuevo registro en la base de datos')
            __update_course(pk)

    except Exception as e:
        print("No es posible actualiza el curso...")
    
    return redirect('home')