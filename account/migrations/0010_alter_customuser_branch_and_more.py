# Generated by Django 4.1.4 on 2023-01-16 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_customuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.warehouse'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_prefix',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.phoneprefix'),
        ),
    ]
