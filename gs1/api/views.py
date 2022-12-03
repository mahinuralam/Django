from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer

from .models import Student
from .serializers import StudentSerializer


# Create your views here.
# view with primay key
def Student_detial(request, pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    return JsonResponse(serializer.data)

# view all data
def Student_detial_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')