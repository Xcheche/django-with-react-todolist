from django.db import models
from django.contrib.auth.models import User

from common.models import BaseModel


class Todo(BaseModel):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    # user who posted this
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title