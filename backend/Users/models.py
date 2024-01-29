# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import default_token_generator
from django.utils.crypto import get_random_string
from uuid import uuid4

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4)

    USER_TYPE_CHOICES = (('S', 'Student'), ('T', 'Teacher'), ('M', 'Manager'),)
    user_type = models.CharField(
        max_length=1,
        choices=USER_TYPE_CHOICES,
        help_text='The type of user.',
        blank=False,
        null=False
    )

    @property
    def is_student(self):
        return self.user_type == 'S'

    @property
    def is_teacher(self):
        return self.user_type == 'T'

    @property
    def is_manager(self):
        return self.user_type == 'M'

    def save(self, *args, **kwargs):
        if not self.pk:
            # Only generate and save the token if the user is being created
            self.generate_token()
        super().save(*args, **kwargs)

    def generate_token(self):
        token = default_token_generator.make_token(self)
        self.auth_token = get_random_string(64)
        self.save(update_fields=['auth_token'])

    def __str__(self):
        return self.username
