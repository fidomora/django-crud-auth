from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from tasks.forms import SignupForm, SigninForm, TaskForm
from tasks.models import Task
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    template_name='home.html'
    return render(request=request,template_name=template_name)

def signup(request):
    errors = ''
    if request.method == 'POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user= User.objects.create_user(
                    username=request.POST['username'], 
                    password=request.POST['password1'])
                user.save()
                login(request, user) # crea la sesion en el usuario
                return redirect('tasks') #redireccionea
                # return HttpResponse('Usuario creado satisfactoriamente')
            except IntegrityError:
                errors = 'El usuario ya existe'
        else:
            errors = 'Password no coincide'

    form = SignupForm
    context={'form':form, 'errors': errors}
    template_name = 'signup.html'
    return render(request=request, template_name=template_name, context=context)


@login_required
def tasks(request):

    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    context={'tasks':tasks}
    template_name='tasks.html'
    return render(request=request,template_name=template_name, context=context)

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    errors = ''

    print(request)
    if request.method =='POST':
        user = authenticate(request=request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            errors = 'Username or password is incorrect'
        else:
            login(request=request, user=user)
            return redirect('tasks')


    form = SigninForm
    context={'form':form, 'errors':errors}
    template_name = 'signin.html'
    return render(request=request, template_name=template_name, context=context)

@login_required
def create_task(request):

    error=''
    # Realiza el guardado si es POST
    if request.method == 'POST':
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            error = 'Proveer datos válidos'

    # Si no redirige, continua en la misma página
    context = { 
        'form': TaskForm,
        'error': error
    }
    template_name = 'create_task.html'
    return render(request=request, template_name=template_name, context=context)

@login_required
def task_detail(request, task_id):
    # task = Task.objects.get(pk=task_id)
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user= request.user)
        form = TaskForm(instance=task)
        context = {'task':task, 'form':form}
        template_name = 'task_detail.html'
        return render(request=request, template_name=template_name, context=context)
    else:
        try:
            task = get_object_or_404(Task, pk=task_id,  user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            context = {'task':task, 'form':form, 'error':"error al actualizar Tarea"}
            template_name = 'task_detail.html'
            return render(request=request, template_name=template_name, context=context)


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')
    
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user = request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    
@login_required   
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    context={'tasks':tasks}
    template_name='tasks.html'    
    return render(request=request, template_name=template_name, context=context)
