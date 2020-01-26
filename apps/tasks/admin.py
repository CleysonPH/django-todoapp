from django.contrib import admin

from .models import Category, Task


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'owner']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'description',
                    'end_date', 'priority', 'status', 'owner']
