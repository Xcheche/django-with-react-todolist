from django.urls import path

from . import views
urlpatterns = [
    path('', views.TodoList.as_view()),
    path('create/', views.TodoListCreate.as_view()),
    path('todos/<int:id>/', views.TodoRetrieveUpdateDestroy.as_view()),
]