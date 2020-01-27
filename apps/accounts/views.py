from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserForm


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            messages.success(
                f'Usuário {user.username} cadastrado com sucesso!')
        print(form.errors)

    template_name = 'accounts/user_form.html'
    form = UserForm()
    context = {
        'title': 'Cadastro de Usuário',
        'form': form
    }

    return render(request, template_name, context)
