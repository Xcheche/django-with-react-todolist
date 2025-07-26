from django.db import models
import uuid
from django.utils import timezone


class BaseModel(models.Model):
    """Abstract base model with common fields for all models."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # set to current time
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        abstract = True