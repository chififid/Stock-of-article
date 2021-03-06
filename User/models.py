from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    username = models.CharField(_('username'), max_length=150, blank=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    subjects = models.ManyToManyField('main.Subject')
    img = models.ImageField(null=True, upload_to='media/avatars')
    key = models.IntegerField(editable=False, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
