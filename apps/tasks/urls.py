from django.urls import path

from . import views


app_name = 'tasks'
urlpatterns = [
    path('categorias/', views.list_categories, name='category-list'),
    path('categoria/criar/', views.create_category,  name='category-create'),
    path('categoria/<int:pk>/editar/', views.edit_category, name='category-edit'),
    path('categoria/<int:pk>/apagar/',
         views.remove_category, name='category-remove'),
    path('tarefas/', views.list_tasks, name='task-list'),
    path('tarefa/criar/', views.create_task, name='task-create'),
    path('tarefa/<int:pk>/editar/', views.edit_task, name='task-edit'),
    path('tarefa/<int:pk>/apagar/', views.remove_task, name='task-remove'),
]
