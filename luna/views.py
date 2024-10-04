from django.shortcuts import redirect, render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime #para usar datetime importar 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #para plantilla de signup
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Task
from .forms import TaskForm



fechaActual= datetime.now()

def home(request):
    return render(request,'inicio.html', {
        'fechaActual': fechaActual #que traiga la fecha actual a la página
    })
def tasks(request):

    tasks = Task.objects.all()
    return render (request, 'tasks.html', {
         'tasks': tasks
    })


#-----------------------
def addtask (request):
     if request.method == 'GET':
          return render(request, 'addtask.html',{
               'form': TaskForm
          })
     else:
          try:
               form = TaskForm(request.POST)
               new_task = form.save(commit=False)
               new_task.user = request.user

               new_task.save()

               return redirect('tasks')
          except:
               return render(request, 'addtask.html', {
                    'form': TaskForm,
                    'error': 'hubo un error'
               })

def updatetasks(request, task_id):
     if request.method == 'GET':
          task = get_object_or_404(Task,pk=task_id)
          form = TaskForm(instance=task)
          return render(request, 'taskdetail.html', {
               'task': task,
               'form': TaskForm
          })
#---------------------------------
def signup(request):
        if request.method == 'GET':
             return render(request, 'signup.html', {
            'form': UserCreationForm
        })
        else:
             if request.POST['password1'] == request.POST['password2']:
                  try:
                       user = User.objects.create_user(
                            username=request.POST['username'],password=request.POST['password1']
                       )
                       user.save()
                       login(request,user)
                       return redirect('tasks')
                  except:
                       return render(request,'signup.html',{
                            'form': UserCreationForm,
                            'error':'Usuario ya existe'
                       })
             else: 
                  return render (request, 'signin.html', {
                 'form': AuthenticationForm,
                 'error': 'Usuario o contraseña incorrectos'
             }) 
                  
def signin (request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })               
    else:

        User=authenticate( request, username = request.POST ['username'], 
                          password = request.POST ['password'])
        if User is None:
            return render (request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            }) 
        else:
            login(request, User)
            return redirect ('tasks')
        
def signout(request):
    logout(request)
    return redirect ('home')
        
 
#         user = User.objects.create_user(
#              username = request.post['username'], 
#              password = request.post ['password']
#         ) #funcion para crear usuarios
#         user.save()
#         return redirect('tasks')

#         return render(request,'signup.html', {
#            'form': UserCreationForm
#        })
# #-------------------------------------------------------------------------------------------------
        
# def signin (request):
#     if request.method == 'GET':
#         return render(request, 'signin.html', {
#             'form': AuthenticationForm
#         })
#     else:

#         User=authenticate( request, username = request.POST ['username'], password = request.POST ['password'])
#         if User is None:
#             return render (request, 'signin.html', {
#                 'form': AuthenticationForm,
#                 'error': 'Usuario o contraseña incorrectos'
#             }) 
#         else: 
#              login(request, User)
#              return redirect ('tasks')


            

 


# Create your views here.
