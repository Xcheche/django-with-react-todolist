from django.test import TestCase
from django.contrib.auth.models import User
from todo.models import Todo


class TodoModelTestCase(TestCase):
    """Test cases for Todo model."""
    
    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_todo_creation(self):
        """Test creating a new todo."""
        todo = Todo.objects.create(
            title='Test Todo',
            memo='Test memo',
            user=self.user
        )
        self.assertEqual(todo.title, 'Test Todo')
        self.assertEqual(todo.memo, 'Test memo')
        self.assertEqual(todo.user, self.user)
        self.assertFalse(todo.completed)
        self.assertIsNotNone(todo.id)
        self.assertIsNotNone(todo.created)
    
    def test_todo_str_representation(self):
        """Test string representation of todo."""
        todo = Todo.objects.create(
            title='Test Todo',
            memo='Test memo',
            user=self.user
        )
        self.assertEqual(str(todo), 'Test Todo')
    
    def test_todo_blank_memo(self):
        """Test creating todo with blank memo."""
        todo = Todo.objects.create(
            title='Test Todo',
            memo='',
            user=self.user
        )
        self.assertEqual(todo.memo, '')
        self.assertEqual(str(todo), 'Test Todo')
