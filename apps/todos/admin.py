from django.contrib import admin
from apps.todos.models import Todos


@admin.register(Todos)
class TodosAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'done', 
                    'done_at', 'start_date', 'days', 'created_at', 'updated_at']
    list_display_links = ['title', 'category', 'done', 
                    'done_at', 'start_date', 'days', 'created_at', 'updated_at']