from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class UserType(models.TextChoices):
    COMMON = 'COMMON', 'Usuário Comum'
    MERCHANT = 'MERCHANT', 'Lojista'


class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    document = models.CharField(max_length=14, unique=True)
    type = models.CharField(max_length=10, choices=UserType.choices)
    password_hash = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
    
    def set_password(self, raw_password):
        self.password_hash = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password_hash)
