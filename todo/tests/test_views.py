from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from todo.models import Todo


class TodoViewTestCase(APITestCase):
    """Test cases for Todo views."""
    
    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.todo = Todo.objects.create(
            title='Test Todo',
            memo='Test memo',
            user=self.user
        )
    
    def test_todo_list_requires_authentication(self):
        """Test that todo list requires authentication."""
        url = reverse('todo:todo-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_todo_list_authenticated(self):
        """Test todo list for authenticated user."""
        self.client.force_authenticate(user=self.user)
        url = reverse('todo:todo-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_todo_create_requires_admin(self):
        """Test that todo creation requires admin permissions."""
        self.client.force_authenticate(user=self.user)
        url = reverse('todo:todo-create')
        data = {'title': 'New Todo', 'memo': 'New memo'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)