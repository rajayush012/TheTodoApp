from django.shortcuts import render,redirect
from .models import Category, Todo

# Create your views here.
def home(request):
    categories = Category.objects
    todos = Todo.objects
    if request.method == 'POST':
        if request.POST['title'] and request.POST['desc'] and request.POST['due'] and request.POST['category']:
            todo = Todo()
            todo.task = request.POST['title']
            todo.desc = request.POST['desc']
            todo.due = request.POST['due']
            todo.category = Category.objects.get(name=request.POST['category'])
            todo.save()
            return redirect("/")
        else:
            return render(request,'list/home.html',{'categories':categories,'todos':todos,'error':"All fields are necessary!"})
    else:
        return render(request,'list/home.html',{'categories':categories,'todos':todos})



    return render(request,'list/home.html',{'categories':categories,'todos':todos})
