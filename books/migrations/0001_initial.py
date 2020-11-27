# Generated by Django 3.0.5 on 2020-11-27 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=50)),
                ('condition', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('availability', models.CharField(max_length=20)),
                ('image1', models.TextField()),
                ('image2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]