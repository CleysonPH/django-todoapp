from django.shortcuts import render
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

            messages.success(request, 'Categoria salva com sucesso!')

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
