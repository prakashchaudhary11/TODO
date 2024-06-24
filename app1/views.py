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