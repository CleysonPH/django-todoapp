from django.urls import path

from . import views


app_name = 'accounts'
urlpatterns = [
    path('usuario/criar/', views.create_user, name='user-create'),
    path('usuario/login/', views.login_user, name='user-login'),
    path('usuario/logout/', views.logout_user, name='user-logout'),
    path('usuario/alterar-senha/', views.user_change_password,
         name='user-change-password'),
    path('usuario/atualizar/', views.update_user,
         name='user-update'),
    path('usuario/perfil/', views.detail_user_profile, name='user-profile-detail'),
    path('usuario/perfil/criar/', views.create_user_profile,
         name='user-profile-create'),
    path('usuario/perfil/alterar/', views.edit_user_profile,
         name='user-profile-edit'),
]
