from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='название')
    slug = models.CharField(max_length=300, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержание')
    preview = models.ImageField(upload_to='articles/', verbose_name='изображение', **NULLABLE)
    creation_date = models.DateField(verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
