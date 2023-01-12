# Generated by Django 4.1.4 on 2023-01-04 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_phoneprefix_prefix_number_alter_warehouse_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_prefix',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.phoneprefix'),
        ),
    ]