from django.shortcuts import render, HttpResponse

# Create your views here.

def test(req):
    return HttpResponse("Welcome to Django!")

def index(req):
    myDict = {'mainh1':'Nithin Sai Krishna','paragraph':'This is the django Portfolio'}
    return render(req,'index.html', context=myDict)


