from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from todo.models import Todo
from .serializers import TodoSerializer
from rest_framework import generics

from rest_framework import generics, permissions
# Create your views here.


class TodoList(generics.ListAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')
    
    
    
#create
class TodoListCreate(generics.CreateAPIView):
    serializer_class = TodoSerializer
    #permission
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAdminUser] # only admin users can create todos
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly] # This allows authenticated users to create todos, but unauthenticated users can only read todos
    #permission_classes = [permissions.AllowAny] # This allows any user to create todos, regardless of authentication status

    # This method is used to get the queryset for the view
    
    def get_queryset(self):
        user = self.request.user # Get the user from the request
        # If the user is authenticated, filter Todos by user, otherwise return an empty queryset
        if user.is_authenticated:
            return Todo.objects.filter(user=user).order_by('-created')
        else:
            return Todo.objects.none()
        ## Save the user when creating a new Todo
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        
        
        
        
        
# Update