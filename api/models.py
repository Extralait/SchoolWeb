from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    speciality = models.CharField("Специальность", max_length=200 ,null=True,blank=True)
    number = models.CharField("Номаер специальности", max_length=20,null=True,blank=True)
    time = models.DateTimeField('Время' ,null=True,blank=True)
    link = models.CharField('Ссылка', unique=True, db_index=True, max_length=200)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.speciality


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

    # Custom User Class
class userProfile(AbstractUser):
    username = None
    first_name = None
    last_name = None

    class RoleChoices(models.TextChoices):
        PARENT = 'parent', 'Родитель'
        ENROLLEE = 'enrollee', 'Абитуриент'

    status = models.CharField('Статус', max_length=10, choices=RoleChoices.choices)
    SNILS = models.IntegerField('СНИЛС', null=True)
    full_name = models.CharField('ФИО', max_length=100)
    email = models.EmailField('Email', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.full_name
