# Generated by Django 3.1 on 2020-12-11 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20201208_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.CharField(max_length=5)),
                ('request_for', models.CharField(max_length=20)),
                ('borrowing_offer', models.IntegerField(blank=True)),
                ('buying_offer', models.IntegerField(blank=True)),
                ('message', models.CharField(max_length=500)),
                ('requester_name', models.CharField(max_length=255)),
                ('requester_email', models.CharField(max_length=255)),
            ],
        ),
    ]