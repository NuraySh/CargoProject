# Generated by Django 4.1.4 on 2023-01-28 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0004_merge_20230128_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_from', models.DecimalField(decimal_places=2, max_digits=3)),
                ('weight_to', models.DecimalField(decimal_places=2, max_digits=3)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight_type', models.CharField(choices=[('fixed', 'Fixed'), ('per_unit', 'Per Unit')], max_length=10)),
                ('liquid', models.BooleanField()),
                ('show_order', models.IntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country')),
            ],
            options={
                'verbose_name': 'Package Cost',
                'verbose_name_plural': 'Package Costs',
            },
        ),
    ]