from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Settings(models.Model):
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Логотип'
    )
    title = models.CharField(
        max_length = 200,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Настройки сайта'
        verbose_name_plural='Настройки сайта'

class About(models.Model):
    title = models.CharField(
        max_length=250,
        verbose_name="Заголовок"
    )
    description = RichTextField(
        verbose_name="Информационный текст"
    )
    image = models.ImageField(
        upload_to="about_image/",
        verbose_name="Фотография"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="О нас"
        verbose_name_plural="О нас"

class Contact(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя пользователя",
        null=True, blank=True
    )
    email = models.EmailField(
        verbose_name="email пользователя"
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Номер телефона",
        null=True, blank=True
    )
    cause = models.CharField(
        max_length=100,
        verbose_name="Причина",
        null=True, blank=True
    )
    message = models.TextField(
        verbose_name="Сообщение",
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Оставленный отзыв"
        verbose_name_plural="Оставленные отзывы"