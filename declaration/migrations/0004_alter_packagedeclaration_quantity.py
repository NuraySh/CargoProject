# Generated by Django 4.1.4 on 2023-03-23 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('declaration', '0003_alter_packagedeclaration_discounted_price_weight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagedeclaration',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
    ]