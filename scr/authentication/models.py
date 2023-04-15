from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Gender(models.TextChoices):
    MALE = 'M', 'Мужской'
    FEMALE = 'F', 'Женский'


class User(AbstractUser):
    middle_name = models.CharField('Отчество', max_length=150, blank=True)
    phone_number = models.CharField('Телефон', max_length=127, blank=True,)
    gender = models.CharField('Пол', max_length=1, choices=Gender.choices, blank=True)
    photo = models.ImageField('Фото', blank=True, upload_to='avatars/', default='avatars/user.png')

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'username': self.username})

    def get_short_name(self) -> str:
        return f'{self.last_name} {self.first_name}'

    def get_full_name(self) -> str:
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    def get_first_order_date(self):
        return self.order_set.order_by('created_at').first().created_at