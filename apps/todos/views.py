from math import ceil
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from apps.todos.forms import TodoForm
from apps.todos.models import Todos
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy 
from django.views.generic import UpdateView, DeleteView, DetailView


def home(request):
    page = request.GET.get('page', '1')
    c = Todos.objects.count() / 3
    plus = 1
    minus = 1
    if int(page) >= ceil(c):
        plus = 0
    if int(page) <= 1:
        minus = 0
    d = int(page) * int(3) 
    limit = 0 + d
    ofset = -3 + d
    todos = Todos.objects.all()[ofset:limit]
    context={
        "todos":todos,
        'next':int(page) + plus,
        'previouse':int(page) - minus,
    }
    return render(request, template_name='index.html', context=context)


def add_todo(request):
    form = TodoForm()
    context = {
        'form':form
    }
    return render(request, template_name='add.html', context=context)


def create_todo(request):
    post = request.POST
    crt = TodoForm(post)
    if crt.is_valid():
        crt.save()
        print('save')
        messages.success(request, message='Object is created')
    else:
        messages.error(request, crt.errors)
    return redirect('add_todo')
    
class Delete(DeleteView):
    model = Todos
    success_url = reverse_lazy('home')
    template_name = 'delete.html'


class Update(UpdateView):
    model = Todos
    form_class = TodoForm
    template_name = 'edit.html'
    success_url = reverse_lazy('home')


class Detail(DetailView):
    template_name = 'detail.html'
    model = Todos