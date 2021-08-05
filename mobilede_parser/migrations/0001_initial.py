# Generated by Django 3.2.5 on 2021-08-04 12:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(db_index=True, max_length=2048)),
                ('name', models.CharField(max_length=1024)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='last updated')),
                ('subscribers', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('site_id', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('url', models.URLField(max_length=2048)),
                ('name', models.CharField(blank=True, max_length=1024)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('vat', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=4096)),
                ('image_url', models.URLField(blank=True, max_length=2048)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='last updated')),
                ('searches', models.ManyToManyField(to='mobilede_parser.Search')),
            ],
        ),
    ]
