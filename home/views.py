from django.shortcuts import HttpResponse, render


# Create your views here.
def index(request):
    return HttpResponse("This is home page")
