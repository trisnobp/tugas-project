from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers

from todolist.forms import TaskForm
from todolist.models import Task

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request): # Menunjukkan to-do-list
    data = Task.objects.filter(user= request.user)
    context = {
        'data': data,
        'user': request.user,
    }
    return render(request, 'todolist_ajax.html', context)

def register(request): # Register akun to-do-list
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request): # Login user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def create_task(request): # Membuat task baru di to-do-list
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST) 
        if form.is_valid():
            task = Task()
            title = request.POST.get('title')
            description = request.POST.get('description')

            task.title = title
            task.description = description   
            task.user = request.user  
            task.save()
        return redirect('todolist:show_todolist')

    context = {'form': form}
    return render(request, 'create-task.html', context)

def add_task(request): # Buat AJAX
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        new_task = Task(
            title = title,
            date = datetime.date.today(),
            description = description,
            user  = request.user, 
        )
        new_task.save()
        return render(request, 'todolist_ajax.html')
    return render(request, 'todolist_ajax.html')

def get_json_data(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def logout_user(request): # Logout
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

