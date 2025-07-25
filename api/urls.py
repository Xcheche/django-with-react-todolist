from django.urls import path

from . import views
urlpatterns = [
    path('', views.TodoList.as_view()),
    path('create/', views.TodoListCreate.as_view()),
    path('todos/<uuid:id>/', views.TodoRetrieveUpdateDestroy.as_view()),
    
    # Test endpoints without authentication (for development/testing)
    path('test/todos/', views.TodoListNoAuth.as_view()),
    path('test/todos/<uuid:id>/', views.TodoRetrieveUpdateDestroyNoAuth.as_view()),
]