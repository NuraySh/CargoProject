# Generated by Django 4.1.4 on 2023-02-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tariff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PenaltyTariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_from', models.DateField()),
                ('till', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fixed_or_percentage', models.CharField(choices=[('fixed', 'Fixed'), ('percentage', 'Percentage')], max_length=10)),
            ],
            options={
                'verbose_name': 'Penalty Tariff',
                'verbose_name_plural': 'Penalty Tariffs',
            },
        ),
    ]