from django.shortcuts import HttpResponse, render


# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is home page")

def about(request):
    return HttpResponse("This is about page")

def servies(request):
    return HttpResponse("This is services page")

def contact(request):
    return HttpResponse("This is contact page")

