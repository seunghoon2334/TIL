from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request): 
    return render(request, 'detail/index.html')
    
def Mysite(request):
    return render(request, 'detail/Mysite.html')

def QnA(request):
    return render(request, 'detail/QnA.html')
    
def Mypage(request):
    return render(request, 'detail/Mypage.html')
    
def SignUp(request):
    return render(request, 'detail/SignUp.html')
    
# def ping(request):
#     return render(request, 'home/ping.html')

# def pong(request):
#     print(request.GET)
#     msg = request.GET.get('message')
#     return render(request, 'home/pong.html', {'msg': msg})
    
# def user_new(request):
#     return render(request, 'home/user_new.html')
    
# def user_read(request):
#     user_id = request.POST.get('user_id')
#     user_password = request.POST.get('user_password')
#     return render(request, 'home/user_read.html', {'user_id': user_id, 
#     'user_password': user_password}) 
    
# def template_example(request):
#     my_dict = {'name': 'kim', 'nickname': 'sh', 'age': 20}
#     my_list = ['폭찹', '김치볶음밥', '짬뽕']
#     my_sentence = 'Life is short, you need python!'
#     messages = ['applge', 'banana', 'cucumber', 'mango']
#     datetimenow = datetime.datetime.now()
#     empty_list = []
#     return render(request, 'home/template_example.html', {'my_dict': my_dict, 'my_list': my_list, 
#     'my_sentence': my_sentence, 'messages': messages, 'datetimenow': datetimenow, 'empty_list': empty_list})
    
# def static_example(request):
#     return render(request, 'home/static_example.html')