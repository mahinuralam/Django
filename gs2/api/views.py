import io

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .serializers import StudentSerializer


# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'DATA CREATED !'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
    
        json_data = JSONRenderer().render(serializer.error)
        return HttpResponse(json_data, content_type='application/json')
