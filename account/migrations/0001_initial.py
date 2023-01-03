# Generated by Django 4.1.4 on 2023-01-03 15:34

import account.helpers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhonePrefix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix_number', models.CharField(choices=[('1', '+99455'), ('2', '+99450'), ('3', '+99451'), ('4', '+99470'), ('5', '+99477'), ('6', '+99499')], max_length=1, verbose_name='phone prefixes')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('1', 'Ganjlik'), ('2', 'Narimanov'), ('3', '20 January')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=25, verbose_name='first name')),
                ('last_name', models.CharField(max_length=25, verbose_name='first name')),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=1)),
                ('phone', models.CharField(max_length=7)),
                ('gov_id', models.CharField(choices=[('1', 'AZE'), ('2', 'AA'), ('3', 'MYI'), ('4', 'DYI')], default='AZE', max_length=12, unique=True)),
                ('pin_code', models.CharField(blank=True, max_length=7, null=True, unique=True)),
                ('client_code', models.CharField(default=account.helpers.id_gen, editable=False, max_length=9, primary_key=True, serialize=False)),
                ('monthly_expense', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('birth_date', models.DateField(null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_blocked', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.warehouse')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('phone_prefix', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.phoneprefix')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
