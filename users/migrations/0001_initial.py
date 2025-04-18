# Generated by Django 3.2.25 on 2025-04-12 02:09

from django.db import migrations, models
import django.utils.timezone
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('is_staff', models.BooleanField(default=False, help_text='Определяет может ли пользователь войти в админ панель', verbose_name='Модератор')),
                ('is_superuser', models.BooleanField(default=False, help_text='Определяет имеет ли пользователь все привелегии', verbose_name='Администратор')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата регистрации')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]
