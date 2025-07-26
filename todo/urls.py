from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.TodoList.as_view(), name='todo-list'),
    path('create/', views.TodoListCreate.as_view(), name='todo-create'),
    path('todos/<uuid:id>/', views.TodoRetrieveUpdateDestroy.as_view(), name='todo-detail'),
]