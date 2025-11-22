from django.shortcuts import render, redirect
from .models import Task

def home_page(request):
    tasks = Task.objects.all()
    return render(request, "home.html", {"tasks":tasks})

def create_post(request):
    if request.method =="POST":
        name = request.POST.get('task')
        time = request.POST.get('time')
        Task.objects.create(name=name,time=time)
        return redirect("home")
    return render(request, "create_post.html")

def delete_task(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')

def edit_task(request,id):
    task = Task.objects.get(id=id)
    if request.method =="POST":
        name = request.POST.get('task')
        time = request.POST.get('time')
        task.name= name
        task.time= time
        task.save()
        return redirect('home')
    return render(request, "create_post.html")
    