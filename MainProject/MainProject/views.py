import requests
from django.shortcuts import render

def __get_courses():
    url = 'http://localhost:8001/api/v1/courses/'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    
    return []

def home(request):
    courses = __get_courses()
    return render(request, 'home.html', {
        'courses': courses
    })