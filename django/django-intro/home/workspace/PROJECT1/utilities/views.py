from django.shortcuts import render
import requests
import datetime
from datetime import date

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')
    
def graduation(request):
    d0 = date(2019, 5, 17)
    d1 = date.today()
    day = d0 - d1
    return render(request, 'utilities/graduation.html', {'d0':d0, 'd1':d1, 'day':day})
    
def imagepick(request):
    return render(request, 'utilities/imagepick.html')
    
def today(request):
    datetimenow = datetime.datetime.now()
    weather_key = 'e4d71ff1449c1cbf2eaa984889ab7fd0'
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?id=1835235&APPID=e4d71ff1449c1cbf2eaa984889ab7fd0'
    response = requests.get(weather_url).json()
    weather = response['weather'][0]['main']
    main = response['main']['temp']-273.15
    wind = response['wind']['speed']
    return render(request, 'utilities/today.html', {'datetimenow':datetimenow, 'weather_key':weather_key, 'response':response, 'weather':weather, 'main':main, 'wind':wind})
    
def ascii_new(request):
    return render(request, 'utilities/ascii_new.html')
    
def ascii_make(request):
    
    text = request.GET.get('text')
    font = request.GET.get('font')
    url = f'https://artii.herokuapp.com/make?text={text}&font={font}'
    response = requests.get(url).text
    
    return render(request, 'utilities/ascii_make.html', {'text':text, 'font':font, 'url':url, 'response':response})
    
def original(request):
    return render(request, 'utilities/original.html')
    
def translated(request):
    print(request.GET)
    msg = request.GET.get('message')
    return render(request, 'utilities/translated.html', {'msg':msg})