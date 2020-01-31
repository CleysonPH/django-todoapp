from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from .forms import UserForm, UserProfileForm, UserUpdateForm
from .models import UserProfile


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


@login_required
def user_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Senha altrerada com sucesso!')
        else:
            messages.error(request, 'Não foi possivel alterar sua senha!')

    template_name = 'accounts/change_user_password.html'
    form = PasswordChangeForm(user=request.user)
    context = {
        'title': 'Trocar Senha',
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            messages.success(request, 'Perfil criado com sucesso!')
            return redirect('accounts:user-profile-detail')

    template_name = 'accounts/user_profile_form.html'
    form = UserProfileForm()
    context = {
        'title': 'Criar Perfil',
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def detail_user_profile(request):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return redirect('accounts:user-profile-create')

    template_name = 'accounts/detail_user_profile.html'
    context = {
        'title': 'Detalhes do Perfil',
        'profile': profile,
    }
    return render(request, template_name, context)


@login_required
def edit_user_profile(request):
    profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil alterado com sucesso!')
            return redirect('accounts:user-profile-detail')

    template_name = 'accounts/user_profile_form.html'
    form = UserProfileForm(instance=profile)
    context = {
        'title': 'Alterar Perfil',
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def update_user(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('accounts:user-profile-detail')

    form = UserUpdateForm(instance=request.user)
    template_name = 'accounts/user_update.html'
    context = {
        'title': 'Atualizar dados',
        'form': form
    }
    return render(request, template_name, context)
