from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()
    user = serializers.StringRelatedField(read_only=True)  # Show username instead of user ID

    class Meta:
        model = Todo
        fields = ['id','title','memo','created','completed','user']
     