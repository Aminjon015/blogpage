from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назваине категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назваине статья')
    content = models.TextField(verbose_name='Описание статьи')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Изображени')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


# Sdelat migratisiyu
# Vipolnit migratsiyu

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарий'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    publisher = models.BooleanField(default=False, verbose_name='Право создания статьи')

    def __str__(self):
        return self.user.username

    def get_photo(self):
        try:
            return self.photo.url
        except:
            return 'https://img.icons8.com/bubbles/100/000000/user.png'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'
