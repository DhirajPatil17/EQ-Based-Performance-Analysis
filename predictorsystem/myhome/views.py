import matplotlib.pyplot as plt
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from myhome.admin import visualizeAdmin
from django.contrib.auth.models import User
from .forms import SignUpForm, Updationform
from .models import Fyit, visualize
from .resources import FyitResources, visualizeResources
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from tablib import Dataset
from .utils import  get_bar_Attendence, get_bar_Marks, get_bar_behaviour, get_bar_plot, get_plot, get_scatter_plot, get_single_bar, get_single_line
import numpy as nm,math
import pandas as pd
import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import joblib 
qs=visualize.objects.all()

behaviour=[x.Behavioral for x in qs]
Attendence=[x.Attendence for x in qs]
Marks=[x.Marks for x in qs]
name=[x.Name for x in qs]
chart=get_plot(name,behaviour)
chart2=get_scatter_plot(behaviour,Marks)
chart3=get_bar_plot(behaviour,Attendence,Marks,name)
chart4=get_bar_behaviour(name,behaviour)
chart5=get_bar_Marks(name,Marks)
chart6=get_bar_Attendence(name,Attendence) 

def loginUser(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in Successfully')
                return HttpResponseRedirect('/allclass')
    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'form':fm})
def base(request):
    if request.user.is_authenticated:
        return render(request,'base.html',{'name':request.user})
    else:
        return redirect('/login')


def registerUser(request):
    
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created succesfully')
            fm.save()
        return redirect('/login')
        
    else:
        fm=SignUpForm()
    return render(request,'register.html',{'form':fm})

def homepage(request):
    if request.user.is_authenticated:
        return render(request,'teacherhome.html')
    else:
        return redirect('/login')
def forms(request):
    return render(request,'form.html')

def simple_upload(request):
    # Excel upload 
    if request.user.is_authenticated:
        context={
        'user':request.user
       }
        if request.method=='POST' and request.FILES['Book2']:
            visualize_resource=visualizeResources()
            dataset=Dataset()
            new_data=request.FILES['Book2']
            if not new_data.name.endswith('xlsx'):
                messages.info(request,"wrong format")
                return render(request,'upload.html')
            imported_data=dataset.load(new_data.read(),format='xlsx')
            for data in imported_data:
                value=visualize(data[0],data[1],data[2],data[3],data[4])
                value.save() 
        elif request.method=='POST' and request.FILES['Book2']:
            Fyit_resource=FyitResources()
            dataset=Dataset()
            new_data=request.FILES['Book2']
            print(new_data)
            if not new_data.name.endswith('xlsx'):
                messages.info(request,"wrong format")
                return render(request,'upload.html')
            imported_data=dataset.load(new_data.read(),format='xlsx')
            for data in imported_data:
                value=Fyit(data[0],data[1],data[2],data[3],data[4])
                value.save() 
        return render(request,'upload.html',context)     
    else:
        return redirect('/login')
def second_year(request):
    if request.user.is_authenticated: 

        return render(request,'second.html')
    else:
        return redirect('/login')

def specific_student(request):
    if request.user.is_authenticated:
        b=request.GET.get('number')
        if request.method=='GET' and b is not None:
            s=qs[int(b)]
            behaviour1=s.Behavioral
            marks1=s.Marks
            name1=s.Name
            Attendence1=s.Attendence
            chart7=get_single_bar(name1,behaviour1,marks1,Attendence1)
            chart8=get_single_line(name1,behaviour1,marks1,Attendence1)
            return render(request,'specific_student.html',{'chart':chart7,'chart1':chart8})
        else:
            return render(request,'specific_student.html')
    else:
        return redirect('/login')
    # y=[y.Marks for y in qs]
def third_year(request):
    if request.user.is_authenticated:
        return render(request,'third.html',{'name':request.user})
    else:
        return redirect('/login')

def last_year(request):
    if request.user.is_authenticated:
        return render(request,'last.html')
    else:
        return redirect('/login')
def prediction(request):
    if request.user.is_authenticated:

        regressor=joblib.load('finalized_model.sav')
        lis=[]
        b=request.GET.get('behaviour')
        a=request.GET.get('attendence')
        if (request.method=='GET') and (b is not None and a is not None):
            print(type(b))
            print(type(a))
            behav=float(b)
            att=float(a)
            lis.append(behav)
            lis.append(att)
            ans=regressor.predict([lis])
            return render(request,'prediction.html',{'ans':ans})
        else:
            return render(request,'prediction.html')
    else:
        return redirect('/login')
def allclass(request):
    if request.user.is_authenticated:
        b=request.GET.get('Plotting')
        print(type(b))
        if request.method=='GET' and b is not None:
            if b=='class_bar':
                return  render(request,'allclass.html',{'chart':chart3})
            elif b=='class_line':
                return  render(request,'allclass.html',{'chart':chart})
            elif b=='Attendence_bar':
                return  render(request,'allclass.html',{'chart':chart6})
            elif b=='Behaviour_bar':
                return  render(request,'allclass.html',{'chart':chart4})
            elif b=='Marks_bar':
                return  render(request,'allclass.html',{'chart':chart5})
            else:
                return render(request,'allclass.html')
        else:
            return render(request,'allclass.html')
    else:
        return redirect('/login')

def insert(request):
    if request.user.is_authenticated:
        return render(request,'insert.html')
    else:
        return redirect('/login')
def update(request,id):
    
        if request.method=='POST':
            pi=visualize.objects.get(pk=id)
            fm=Updationform(request.POST,instance=pi)
            if fm.is_valid():
                fm.save() 
        else:
            pi=visualize.objects.get(pk=id)
            fm=Updationform(instance=pi)
        return render(request,'update.html',{'form':fm})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')
def insert2(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            name=request.POST.get('Name')
            behaviour=request.POST.get('Behavioral')
            Attendence=request.POST.get('Attendence')
            Marks=request.POST.get('Marks')
            data=visualize(Name=name,Marks=Marks,Behavioral=behaviour,Attendence=Attendence)
            data.save()
            myqs=visualize.objects.all()
            return render(request,'insert2.html',{'qs':qs})
        else:
            myqs=visualize.objects.all()
            return render(request,'insert2.html',{'qs':myqs})
    else:
        return redirect('/login')
def My(request):
    return render(request,'my.html')
def delete(request,id):
    if request.method=="POST":
        pi=visualize.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/insert2')
   




            


     
   

