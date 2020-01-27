from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
                request, f'Usuário {user.username} cadastrado com sucesso!')
        print(form.errors)

    template_name = 'accounts/user_form.html'
    form = UserForm()
    context = {
        'title': 'Cadastro de Usuário',
        'form': form
    }

    return render(request, template_name, context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        messages.error(request, 'Usuário ou senha inválidos.')

    template_name = 'accounts/login_user.html'
    context = {
        'title': 'Login'
    }
    return render(request, template_name, context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('accounts:user-login')
