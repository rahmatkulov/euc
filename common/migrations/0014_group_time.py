# Generated by Django 5.2.2 on 2025-06-14 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0013_alter_group_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='time',
            field=models.TimeField(null=True, verbose_name='time'),
        ),
    ]
