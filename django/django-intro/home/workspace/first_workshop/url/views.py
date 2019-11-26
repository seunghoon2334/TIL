import random
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request): 
    return render(request, 'index.html')
    
def info(request):
    return render(request, 'info.html')
    
def student(request, name):
    students = {'홍길동':'10', '김길동':'14', '박길동':'28'}
    age = students[name]
    return render(request, 'student.html', {'name': name, 'age': age})