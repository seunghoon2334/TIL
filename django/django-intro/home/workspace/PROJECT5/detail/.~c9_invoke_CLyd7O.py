from django.shortcuts import render

classroom = {'박길동': 28, '홍길동': 29, '김길동': 27}
# Create your views here.
def info(request):
    teacher = '이길동'
    return render(request, 'info.html', {'classroom': classroom, 'teacher': teacher})
    
def student(request, name):
    age = classroom.get(name,' unknown')
    return render(request, 'student.html', {'age': age, 'name': name})






