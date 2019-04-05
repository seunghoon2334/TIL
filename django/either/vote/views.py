from django.shortcuts import render, redirect
from .models import Question, Answer, Count

# Create your views here.
def index(request):
    questions = Question.objects.all()
    return render(request, 'vote/index.html', {'questions': questions})
    
def new(request):
    if request.method == 'POST':
        question = Question()
        title = request.POST.get('title')
        option_A = request.POST.get('option_A')
        option_B = request.POST.get('option_B')
        question.title = title
        question.option_A = option_A
        question.option_B = option_B
        question.save()
        return redirect('vote:index')
    else:
        return render(request, 'vote/new.html')
        
def detail(request, question_pk):
    question = Question.objects.get(id=question_pk)
    select_A = question.count_set.filter(count='A')
    select_B = question.count_set.filter(count='B')
    select_A = len(select_A)
    select_B = len(select_B)
    if select_A == 0 and select_B == 0:
        select_A_per = 0
        select_B_per = 0
    else:
        select_A_per = (select_A / (select_A + select_B)) * 100
        select_B_per = (select_B / (select_A + select_B)) * 100
    answers = question.answer_set.all()
    
    context = {
        'question' : question,
        'answers' : answers,
        'select_A' : select_A,
        'select_B' : select_B,
        'select_A_per' : select_A_per,
        'select_B_per' : select_B_per
    }
    return render(request, 'vote/detail.html', context)

def select(request, question_pk):
    question = Question.objects.get(id=question_pk)
    choice = request.GET.get('option')
    count = Count()
    count.count = choice
    count.question = question
    count.save()
    return redirect('vote:detail', question.pk)

def create_comment(request, question_pk):
    answer = Answer()
    question = Question.objects.get(pk=question_pk)
    answer.user = request.POST.get('user')
    answer.comment = request.POST.get('comment')
    answer.question = question
    answer.save()
    return redirect('vote:detail', question_pk)
    
        