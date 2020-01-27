from django.urls import path

from . import views


app_name = 'accounts'
urlpatterns = [
    path('usuario/criar/', views.create_user, name='user-create')
]
