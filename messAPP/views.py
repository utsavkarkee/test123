from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from messAPP.models import StudentData

def form(request):
    return render(request,'messAPP/index.html')

def login(request):
    rollno = request.POST['rollNum']
    result = StudentData.objects.get(roll_number = rollno)
    return render(request,'messAPP/details.html',{'result':result})

def dbRequest(request):
    frm = request.POST["frm"]
    to  = request.POST["to"]
    return HttpResponse(frm +" "+ to)
