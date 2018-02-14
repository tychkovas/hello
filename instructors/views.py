from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound
from instructors.models import Instructor


def hello(request):
    #print(request.META)      
    return render(request, 'index.html')

def instructors_list(request):
    instructors = Instructor.objects.all()   
    return render(request, 'instructors.html', {"instructors_list":instructors})


def http(request):
    response = render(request,'http.html')
    #print(request.META)          
    return response

def hello_python(request):
	return render(request, 'python.html')

def sum_two(request, a, b):
	s = int(a) + int(b)
	print("Hi!!");
	print(a,b);
	return HttpResponse(s)