from apps.todos.views import Update, home, add_todo, create_todo, Delete, Detail
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('add/', add_todo, name='add_todo'),
    path('create/', create_todo, name='create'),
    path('delete/<int:pk>', Delete.as_view(), name='delete'),
    path("update/<int:pk>", Update.as_view(), name='update'),
    path("detail/<int:pk>", Detail.as_view(), name='detail'),
]