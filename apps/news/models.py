from django.db import models
from ckeditor.fields import RichTextField
from django_resized.forms import ResizedImageField


# Create your models here.
class News(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = RichTextField(
        verbose_name="Описание"
    )
    image = ResizedImageField(
        force_format="WEBP",
        upload_to="news_image/",
        quality=100,
        verbose_name="Фотография"
    )
    created = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
        null=True, blank=True
    )
    created_2 = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        null=True, blank=True
    )
    image2 = ResizedImageField(
        force_format="WEBP",
        upload_to="news_image/",
        quality=100,
        verbose_name="Фотография2"
    )
    description2 = RichTextField(
        verbose_name="Описание2"
    )
    description3= models.TextField(
        verbose_name="Описание3"
    )
    description4 = RichTextField(
        verbose_name="Описание2"
    )
    image4 = ResizedImageField(
        force_format="WEBP",
        upload_to="news_image/",
        quality=100,
        verbose_name="Фотография2"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Новость"
        verbose_name_plural="Новости"

    