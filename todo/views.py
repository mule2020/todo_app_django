from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, CreateTask
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
@login_required(login_url = 'login')
def index(request):
    if request.user.is_authenticated:
        pk = request.user
        form = CreateTask(request.POST)
        if request.method == 'POST':

            form = CreateTask(request.POST)
            if form.is_valid():
                todos = TodoApp.objects.create(
                    user = User.objects.get(username=pk),
                    title = form.cleaned_data['title']

                )

                todos.save()
                messages.success(request, "new task added")
                return redirect('index')
        todos = TodoApp.objects.filter(user = pk).order_by('-date_created',)
    else:
        return redirect('login')

    context = {'todos': todos,'form': form,}
    return render(request, 'base/dashboard.html', context)
def about(request):
    return render(request, 'base/home.html')

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password  = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, ' user Credential mis match!')
    return render(request, 'base/login.html')
def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                messages.success(request, 'User Created for '+  username)
                return redirect('login')




        context = {'form': form,}
    return render(request, 'base/register.html', context)
@login_required(login_url = 'login')
def updateTask(request, pk):
    todo = TodoApp.objects.get(id=pk)
    form = CreateTask(instance=todo)
    if request.method == "POST":
        form = CreateTask(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task Updated successfully ')
            return redirect('index')
    context = {'form': form}
    return render(request,"base/update.html", context)

@login_required(login_url = 'login')
def deleteTask(request, pk):
    todo = TodoApp.objects.get(id=pk)
    if request.method == "POST":
        todo.delete()
        messages.success(request, 'Task DELETED successfully ')
        return redirect('index')
    context = {'todo': todo}
    return render(request, 'base/delete.html', context)


def error_404(request, exception):
        data = {'exception': exception}
        return render(request,'base/404.html', data)