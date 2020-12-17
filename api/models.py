from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


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
    SNILS = models.IntegerField('СНИЛС',null=True)
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

class Event(models.Model):
    organizer = models.CharField("Организатор", max_length=60)
    date = models.DateField('Дата проведения')
    link = models.SlugField('Ссылка', unique=True)

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.organizer


class Organization(models.Model):
    name = models.CharField('Название направления', max_length=64)
    number = models.TextField('Код направления', blank=True, null=True)
    USE = models.TextField('ЕГЭ', blank=True, null=True)
    work = models.TextField('Трудоустройство', blank=True, null=True)
    practice = models.TextField('Практика', blank=True, null=True)
    internship = models.TextField('Стажировки', blank=True, null=True)
    place = models.IntegerField('Бюджетных мест', blank=True, null=True)
    price = models.IntegerField('Цена обучения', blank=True, null=True)
    score = models.TextField('Баллы прошлых лет', blank=True, null=True)
    min_score = models.TextField('Минимальные баллы', blank=True, null=True)
    disciplines_list = models.TextField('Список дисциплин', blank=True, null=True)
    best_students = models.TextField('Список дисциплин', blank=True, null=True)
    offer = models.ForeignKey('self', verbose_name='Предложение', on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(Event, verbose_name='Вебинар', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Направлени'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return self.name
