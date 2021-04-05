from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myfun(request):
    return HttpResponse("Hiiii")
def testfun(request):
    return render(request,'a.html')    
def plfun(request):
    return render(request,'add plants.html')    
def stfun(request):
    return render(request,'add staffs.html')    
def loginfun(request):
    return render(request,'login.html')    
def dashfun(request):
    return render (request,'admin dashboard1.html')    
def bsfun(request):
    return render (request,'bs.html')  
def formfun(request):
    return render (request,'form.html')    
def abfun(request):
    return render (request,'ab.js')   
def demofun(request):
    return render (request,'demo2.html') 
def fbfun(request):
    return render (request,'fb.html')  
def fb2fun(request):
    return render (request,'fb2.html')         
def afun(request):
    return render (request,'a.html')   
def ffun(request):
    return render (request,'f.html')    
def calcfun(request):
    return render (request,'home.html')        