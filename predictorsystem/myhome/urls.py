from unicodedata import name
from django.contrib import admin
from django.urls import path
from pyrsistent import v
from myhome import views

urlpatterns = [
   path('login',views.loginUser,name="index"),
   path('register',views.registerUser,name="register"),
   path('home',views.homepage,name="home"),
   path('my',views.My,name="my"),
   path('form',views.forms,name="form"),
   path('simple',views.simple_upload,name="simple"),
   path('second',views.second_year,name="second"),
   path('third',views.third_year,name="third"),
   path('last',views.last_year,name="last"),
   path('specific_student',views.specific_student,name="specific"),
   path('prediction',views.prediction,name="prediction"),
   path('allclass',views.allclass,name='allclass'),
   path('logout',views.user_logout,name="logout"),
   path('insert',views.insert,name="insert"),
   path('<int:id>',views.update,name="update"),
   path('delete/<int:id>',views.delete,name="deletedata"),
   path('insert2',views.insert2,name="insert2"),
   path('base',views.base,name="base")
  
   
]