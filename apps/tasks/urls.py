from django.urls import path

from . import views


app_name = 'tasks'
urlpatterns = [
    path('categoria/criar', views.create_category,  name='create-category')
]