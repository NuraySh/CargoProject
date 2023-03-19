# Generated by Django 4.1.4 on 2023-03-19 17:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('declaration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageStatusHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('date_changed', models.DateTimeField(default=django.utils.timezone.now)),
                ('declaration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='declaration.packagedeclaration')),
            ],
            options={
                'verbose_name': 'Status History',
                'verbose_name_plural': 'Status Histories',
                'ordering': ['-date_changed'],
            },
        ),
    ]
