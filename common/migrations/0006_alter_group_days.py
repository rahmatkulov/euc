# Generated by Django 5.2.2 on 2025-06-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_group_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='days',
            field=models.CharField(choices=[('Du Chor Ju', 'Du Chor Ju'), ('Se Pay Shan', 'Se Pay Shan')], verbose_name='days'),
        ),
    ]
