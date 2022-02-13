from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('create/', views.register),
    path('signin', views.signin),
    path('jobs/',views.jobs),
    path('jobs/new/', views.addjob),
    path('jobs/new/create_job', views.create_job),
    path('jobs/new/<int:job_id>/add_job2', views.add_job2),
    path('jobs/<int:job_id>/add_job/', views.add_job),
    path('jobs/<int:job_id>/remove_job/', views.remove_job),
    path('logout', views.logout),
    path('jobs/logout', views.logout),
    path('jobs/<int:job_id>/logout',views.logout),
    path('jobs/<int:job_id>/update', views.update),
    path('jobs/<int:job_id>/edit', views.edit),
    path('jobs/<int:job_id>/delete/', views.delete),
    path('jobs/<int:job_id>/view', views.jobpage),
    path('jobs/<int:job_id>/new_task/', views.newTask),
    path('jobs/<int:job_id>/new_task/create_task', views.createTask),
    path('jobs/<int:job_id>/<int:task_id>/add_task/', views.add_task),
    path('jobs/<int:task_id>/deleteTask/', views.deleteTask),
    path('jobs/<int:task_id>/editTask', views.editTask),
    path('jobs/<int:task_id>/updateTask', views.updateTask),
    path('jobs/new/<int:job_id>/<int:vehicle_id>/add_vehicles', views.add_vehicle)
]