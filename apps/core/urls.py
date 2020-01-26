from django.urls import path

from . import views


app_name = 'core'
urlpatterns = [
    path('', views.hello_world, name='hello-world'),
]
