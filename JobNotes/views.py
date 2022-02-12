from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Job, Vehicle, Equipment, Task
from django.db import transaction
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        errors= User.objects.register_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')

        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user=User.objects.create(first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=pw_hash)
        request.session['user_id'] = new_user.id
        return redirect('/jobs')
    return redirect('/')

def signin(request):
    errors= User.objects.login_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        this_user= User.objects.filter(email=request.POST['email'])[0]
        request.session['user_id']=this_user.id
        return redirect('/jobs')

def jobs(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user=User.objects.filter(id = request.session['user_id'])
    context={
        'user': this_user[0],
        'all_the_jobs':Job.objects.all(),
        'all_the_tasks':Task.objects.all()
    }
    return render(request,'jobs.html', context)

def add_job(request, job_id):
    this_job=Job.objects.get(id=job_id)
    this_job.active == True;
    return redirect('/jobs')

def remove_job(request, job_id):
    this_job=Job.objects.get(id=job_id)
    this_job.active == False;
    return redirect('/jobs')



def logout(request):
    request.session.flush()
    return redirect('/')

def update(request, job_id):
    errors=Job.objects.job_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/jobs/{job_id}/edit')
    else:
        this_user=User.objects.get(id = request.session['user_id'])
        this_job=Job.objects.get(id=job_id)
        this_job.title=request.POST['title']
        this_job.description=request.POST['description']
        this_job.location=request.POST['location']
        this_job.uploader=this_user
        this_job.save()
        return redirect('/jobs')

def delete(job_id):
    this_job=Job.objects.get(id=job_id)
    this_job.delete()
    return redirect('/jobs')

def deleteTask(task_id):
    this_task=Task.objects.get(id=task_id)
    this_task.delete()
    return redirect('/jobs')

def edit(request, job_id):
    if 'user_id' not in request.session:
        return redirect('/')
    this_job=Job.objects.get(id=job_id)
    context={
        'this_job':this_job
    }
    return render(request,'edit.html',context)


def jobpage(request, job_id):
    if 'user_id' not in request.session:
        return redirect('/')
    this_job=Job.objects.get(id=job_id)
    context={
        'job':this_job
    }
    return render(request,'details.html',context)

def create_job(request):
    errors= Job.objects.job_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/jobs/new')
    else:
        this_user=User.objects.get(id = request.session['user_id'])
        new_job=Job.objects.create(
            title=request.POST['title'],
            date=request.POST['date'],
            description=request.POST['description'],
            location=request.POST['location'],
            uploader=this_user)
        new_job.active == True;
        return redirect(f'/jobs/new/{new_job.id}/add_job2')


def add_job2(request, job_id):
    this_job=Job.objects.get(id=job_id)
    context={
        'this_job':this_job,
        'all_vehicles':Vehicle.objects.all(),
        'all_users':User.objects.all()
    }
    return render(request,'add_job_2.html', context)

def create_job2(request, job_id, user_id, vehicle_id):
    this_job=Job.objects.get(id=job_id)
    this_vehicle=Job.objects.get(id=vehicle_id)
    this_user-User.objects.get(id=user_id)

    return redirect()

def addjob(request):

    return render(request,'add_job.html')

def newTask(request, job_id):
    this_job=Job.objects.get(id=job_id)
    return render(request,'add_task.html')

def editTask(request, task_id):
    if 'user_id' not in request.session:
        return redirect('/')
    this_task=Task.objects.get(id=task_id)
    context={
        'this_task':this_task
    }
    return render(request,'editTask.html',context)

def updateTask(request, task_id):
        this_task=Task.objects.get(id=task_id)
        this_task.name=request.POST['name']
        this_task.description=request.POST['description']
        this_task.timein=request.POST['timein']
        this_task.timeout=request.POST['timeout']
        this_task.save()
        return redirect('/jobs')

def createTask(request, job_id):
    #this_user=User.objects.get(id = request.session['user_id'])
    this_job=Job.objects.get(id=job_id)
    new_task=Task.objects.create(
        name=request.POST['name'],
        description=request.POST['description'],
        timein=request.POST['timein'],
        timeout=request.POST['timeout']
    )
    return redirect(f'/jobs/{this_job.id}/{new_task.id}/add_task/')

def add_task(job_id,task_id):
    this_task=Task.objects.get(id=task_id)
    this_job=Job.objects.get(id=job_id)
    this_job.tasks.add(this_task)
    return redirect('/jobs')