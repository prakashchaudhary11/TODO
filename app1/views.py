from django.shortcuts import render,redirect
from .models import todo

# Create your views here.

def home(request):
    todo_obj = todo.objects.all()
    data = {'todos':todo_obj}
    return render(request,"index.html",context=data)

def create(request):

    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')

        todo.objects.create(name=name,description=description,status=status)

        return redirect('home')
    return render(request,"create.html")


def edit(request,pk):
    todo_obj = todo.objects.get(id=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        description =request.POST.get('description')
        status = request.POST.get('status')

        todo_obj.name = name
        todo_obj.description = description
        todo_obj.status = status
        todo_obj.save()

        return redirect('home')

    return render(request,'edit.html',context={'todos':todo_obj})

def delete(request,pk):
    todo_obj = todo.objects.get(id=pk)
    todo_obj.delete()
    return redirect('home')
