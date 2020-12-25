# Generated by Django 3.0.5 on 2020-12-25 20:10

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('fname', models.CharField(max_length=255)),
                ('mname', models.CharField(blank=True, max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('yearOfEnrollment', models.CharField(blank=True, max_length=4)),
                ('yearOfGraduation', models.CharField(blank=True, max_length=4)),
                ('dept', models.CharField(blank=True, max_length=255)),
                ('roll', models.CharField(blank=True, max_length=10)),
                ('hostel', models.CharField(blank=True, max_length=255)),
                ('is_active', models.BooleanField(blank=True, default=False)),
                ('is_staff', models.BooleanField(blank=True, default=False)),
                ('wishlist', jsonfield.fields.JSONField(blank=True, default=dict)),
                ('liked_blogs', jsonfield.fields.JSONField(blank=True, default=dict)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
