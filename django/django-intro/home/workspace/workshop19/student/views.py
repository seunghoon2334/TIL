from django.shortcuts import render, redirect
from .models import Student

# Create your views here.
def index(request):
    student = Student.objects.all()
    return render(request, 'student/index.html', {'student':student})
    
def new(request):
    if request.method == 'POST':
        student = Student()
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.birthday = request.POST.get('birthday')
        student.age = request.POST.get('age')
        student.save()
        return redirect('student:detail', student.pk)
    else:
        return render(request, 'student/new.html')
    
def detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student/detail.html', {'student':student})
    
def edit(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk)
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.birthday = request.POST.get('birthday')
        student.age = request.POST.get('age')
        student.save()
        return redirect('student:detail', student.pk)
    else:
        student = Student.objects.get(pk=pk)
        return render(request, 'student/edit.html', {'student':student})
    
def delete(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student:index')
    else:
        return redirect('student:detail', student.pk)