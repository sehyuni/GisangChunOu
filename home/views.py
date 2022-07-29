from django.shortcuts import render, redirect
from .models import Date
from django.utils import timezone

data ={}
# Create your views here.
def home_mem(request):
    return render(request, 'home_mem.html')

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def mypage(request):
    return render(request, 'mypage.html')

def newmember(request):
    return render(request, 'newmember.html')

def ranking(request):
    return render(request, 'ranking.html')

def mostvoted():
#    today = Date.date.get(id=1)
    today = Date.objects.get(date="2022-07-28")
    sunny = today.sunny
    rainny = today.rainny
    snow = today.snow

    A =[sunny, rainny, snow]

    if(max(A)==sunny):
        most = "sunny"
    elif(max(A)==rainny):
        most = "rainny"
    elif(max(A)==snow):
        most = "snow"
    
    return most

def forecast(request):

    if(request.method=='POST'):
        selected_weather = request.POST['weather']
        today = Date.objects.get(date="2022-07-28")

        if(selected_weather == 'sunny'):
            today.sunny +=1
            today.save()
        if(selected_weather == 'rainny'):
            today.rainny +=1
            today.save()
        if(selected_weather == 'snow'):
            today.snow +=1
            today.save()
        #mostvoted=mostvoted()
        data={'weather':mostvoted()}
        print(data['weather'])
        #return redirect('/home_mem/')
        return render(request,'home_mem.html',data)
    return render(request)
