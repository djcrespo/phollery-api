from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from .managers import UserManager
from apps.events.models import Event

ROL_CHOICES = (
    ('employee', 'Employee'),
    ('guest', 'Guest')
)


class User(AbstractUser):

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Cambia 'custom_user_set' por el nombre que prefieras
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Cambia 'custom_user_permissions' por el nombre que prefieras
        blank=True
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # Rol dentro del sistema
    role = models.CharField(max_length=100, choices=ROL_CHOICES, default='guest')

    # Eventos
    events = models.ManyToManyField(Event, related_name='events', blank=True)

    objects = UserManager()

    def __str__(self):
        return self.email
