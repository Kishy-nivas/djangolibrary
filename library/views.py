from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,'library/base.html',{'msg':"welcome to central library"})