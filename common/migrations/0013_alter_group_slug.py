# Generated by Django 5.2.2 on 2025-06-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0012_group_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(max_length=256, verbose_name='slug'),
        ),
    ]
