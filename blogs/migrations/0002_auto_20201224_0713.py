# Generated by Django 3.1 on 2020-12-24 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='publisher_email',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='publisher_dept',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
