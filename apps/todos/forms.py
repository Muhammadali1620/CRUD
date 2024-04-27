from django import forms
from apps.todos.models import Todos
#exclude = ('title', 'description', 'category', 'user', 'start_date', 'days')



class TodoForm(forms.ModelForm):
    class Meta:
        model = Todos
        exclude = ('done_at', 'done')