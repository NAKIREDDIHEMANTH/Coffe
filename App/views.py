from django.shortcuts import render,redirect
from .models import Reg
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

# Create your views here.
class Register(View):

    def get(self,request):

        return render(request,'register.html')
    def post(self,request):

        fn=request.POST['t1']
        ln=request.POST['t2']
        un=request.POST['t3']
        pw=request.POST['t4']
        rpw=request.POST['t5']
        em=request.POST['t6']
        print(f"Captured data: {fn}, {ln}, {un}, {em}, {pw}, {rpw}")

        
        if pw != rpw:
            return HttpResponse("Passwords do not match. Please try again.")

        
        store = Reg(FirstName=fn, LastName=ln, UserName=un, Password=pw,
                    RePassword=rpw, Email=em)
        store.save()
        return render(request,"login.html")
def login(request):
    return render(request,'login.html')
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,'about.html')
def products(request):
    return render(request,'products.html')
def customers(request):
    return render(request,'customers.html')


