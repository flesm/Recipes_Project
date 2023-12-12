from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser, models.Model):
    is_admin = models.BooleanField(default=False, blank=True)


# class Users(AbstractUser):
#     user_id = models.AutoField(primary_key=True, verbose_name="Номер пользователя")
#     username = models.CharField(max_length=255, verbose_name="Имя")
#     email = models.EmailField(max_length=255, verbose_name="Эл. Почта")
#     password = models.CharField(max_length=255, verbose_name="Пароль")
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='users_permissions',
#         blank=True,
#     )
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='users_groups',
#         blank=True,
#     )
#
#     def __str__(self):
#         return self.username