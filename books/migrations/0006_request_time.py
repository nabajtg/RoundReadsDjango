# Generated by Django 3.1 on 2020-12-12 05:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20201212_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
