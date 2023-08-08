# Generated by Django 4.2.3 on 2023-08-07 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='название')),
                ('slug', models.CharField(blank=True, max_length=300, null=True, verbose_name='slug')),
                ('content', models.TextField(verbose_name='содержание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='articles/', verbose_name='изображение')),
                ('creation_date', models.DateField(verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]