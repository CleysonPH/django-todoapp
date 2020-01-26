from django.shortcuts import render

from .forms import CategoryForm, TaskForm


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            category = form.save(commit=False)
            category.owner = request.user
            category.save()

    template_name = 'tasks/category_form.html'
    form = CategoryForm()
    context = {
        'title': 'Criar nova categoria',
        'form': form,
    }
    return render(request, template_name, context)
