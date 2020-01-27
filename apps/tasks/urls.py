from django.urls import path

from . import views


app_name = 'tasks'
urlpatterns = [
    path('categoria/criar/', views.create_category,  name='category-create'),
    path('categorias/', views.list_categories, name='category-list'),
    path('categoria/<int:pk>/editar/', views.edit_category, name='category-edit'),
    path('categoria/<int:pk>/apagar/',
         views.remove_category, name='category-remove'),
]
