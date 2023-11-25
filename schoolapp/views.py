from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core import serializers
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, Course




from django.shortcuts import render, redirect

from .models import *
def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            messages.info(request,"Application submit")
            form.save()

            return redirect('/apply')


    return render(request, 'apply.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'apply.html', {'form': form})


# AJAX
def load_cities(request):
    department_id = request.GET.get('department_id')
    cities = Course.objects.filter(department_id=department_id).all()
    return render(request, 'course_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


# Create your views here.


def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def add(request):
    return render(request,'apply.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        # user.save()
        # print('login submit')
        # auth.login(request, user)


        if user is not None:
            auth.login(request, user)
            return redirect('apply/')
        else:
            messages.info(request, "login submit")
            return redirect("login")

    return render(request, "login.html",)

def application(request):




    if request.method=='POST':


        username=request.POST['Name']
        date_of_birth = request.POST['date-of-birth']
        age = request.POST['Age']
        gender= request.POST['Gender']
        phone_number = request.POST['PHONE NUMBER']
        email = request.POST['email']
        address = request.POST['Address']
        department= request.POST['Department']
        purpose=request.POST['Purpose']
        materials_provide=request.POST['Materials_provide']


        user=User.objects.create_user(materials_provide=materials_provide,purpose=purpose,username=username,date_of_birth=date_of_birth,age=age,gender=gender,phone_number=phone_number,email=email,address=address,department=department)
        user.save();

        return redirect('application')

    else:
        return render(request, ('apply.html'))

# def load_courses(request):
#     department_id = request.GET.get('department')
#     courses = Course.objects.filter(department_id=department_id).order_by('name')
#
#
#     return render(request, 'course_dropdown_list_options.html', {'courses': courses})

def register(request):
    if request.method=='POST':

        username=request.POST['username']

        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('/login')
            # elif User.objects.filter(password=password).exists():
            #     messages.info(request, "password is taken")
                return redirect('login')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect("login")
        else:
            messages .info (request,"password not matching")
            return redirect('login')

            return redirect('login')

    return render(request, ('register.html','login'))







