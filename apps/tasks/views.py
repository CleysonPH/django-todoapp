from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .forms import CategoryForm, TaskForm
from .models import Category, Task


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.owner = request.user
            category.save()

            messages.success(
                request, f'Categoria {category.name} salva com sucesso!')

    template_name = 'tasks/category_form.html'
    form = CategoryForm()
    context = {
        'title': 'Criar nova categoria',
        'form': form,
    }
    return render(request, template_name, context)


def list_categories(request):
    template_name = 'tasks/category_list.html'
    category_list = Category.objects.filter(owner=request.user)

    context = {
        'title': 'Lista de Categorias',
        'category_list': category_list,
    }

    return render(request, template_name, context)


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            return redirect('tasks:category-list')

    template_name = 'tasks/category_form.html'
    form = CategoryForm(instance=category)
    context = {
        'title': 'Editar dados da categoria',
        'form': form,
    }

    return render(request, template_name, context)


def remove_category(request, pk):
    category = get_object_or_404(Category, pk=pk, owner=request.user)
    category.delete()
    messages.success(
        request, f'Categoria {category.name} apagada com sucesso')

    return redirect('tasks:category-list')


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            form.save_m2m()

            messages.success(
                request, f'Tarefa {task.name} salva com sucesso!')

    template_name = 'tasks/task_form.html'
    form = TaskForm()
    context = {
        'title': 'Criar nova tarefa',
        'form': form,
    }
    return render(request, template_name, context)


def list_tasks(request):
    template_name = 'tasks/task_list.html'
    task_list = Task.objects.filter(owner=request.user).exclude(status='CD')

    context = {
        'title': 'Lista de Tarefas',
        'task_list': task_list,
    }

    return render(request, template_name, context)


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('tasks:task-list')

    template_name = 'tasks/task_form.html'
    form = TaskForm(instance=task)
    context = {
        'title': 'Editar dados da tarefa',
        'form': form,
    }

    return render(request, template_name, context)


def remove_task(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    task.delete()
    messages.success(
        request, f'Tarefa {task.name} apagada com sucesso')

    return redirect('tasks:task-list')
