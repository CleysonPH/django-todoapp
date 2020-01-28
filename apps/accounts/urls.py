from django.urls import path

from . import views


app_name = 'accounts'
urlpatterns = [
    path('usuario/criar/', views.create_user, name='user-create'),
    path('usuario/login/', views.login_user, name='user-login'),
    path('usuario/logout/', views.logout_user, name='user-logout'),
    path('usuario/alterar-senha/', views.user_change_password,
         name='user-change-password'),
]
