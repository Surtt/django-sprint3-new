from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    is_published = models.BooleanField(
        default=True, verbose_name='Опубликовано'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Location(models.Model):
    name = models.CharField(max_length=256, verbose_name='Местоположение')
    is_published = models.BooleanField(
        default=True, verbose_name='Опубликовано'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(verbose_name='Дата публикации')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория',
    )
    is_published = models.BooleanField(
        default=True, verbose_name='Опубликовано'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
