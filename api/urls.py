from django.urls import path

from .import views
urlpatterns = [
    path('todos/', views.TodoList.as_view()),
    path('todos/create/', views.TodoListCreate.as_view()),
    #path('todos/<int:pk>/update/', views.TodoListUpdate.as_view()),
]