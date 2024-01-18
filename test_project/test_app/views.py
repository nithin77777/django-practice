from django.shortcuts import render, HttpResponse

# Create your views here.

<<<<<<< HEAD
def test(req):
    return HttpResponse("Welcome to Django!")
=======

>>>>>>> 986bd7e63af788c4ff10dc83cb6155c12946e7f8

def index(req):
    myDict = {'mainh1':'Nithin Sai Krishna','paragraph':'This is the django Portfolio'}
    return render(req,'index.html', context=myDict)
<<<<<<< HEAD


=======
>>>>>>> 986bd7e63af788c4ff10dc83cb6155c12946e7f8
