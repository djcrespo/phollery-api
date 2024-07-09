from django.db import models
from uuid import uuid4


# Create your models here.
class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    event_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    # photos
    # template

    def __str__(self):
        return f"{self.id}"
