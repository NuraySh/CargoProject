# Generated by Django 4.1.4 on 2023-03-23 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_faq_category_localwarehouse_alter_contactus_options_and_more'),
        ('declaration', '0005_alter_packagedeclaration_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagedeclaration',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.currency'),
        ),
    ]
