from django.db import models
from uuid import uuid4


# Create your models here.


# Fotos
class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.FileField(upload_to='photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.id}"


# Eventos
class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    event_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    photos = models.ManyToManyField(Photo, related_name='event_photos')
    template = models.FileField(upload_to='templates/', null=True, blank=True)

    def __str__(self):
        return f"{self.id}"
