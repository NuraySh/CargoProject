# Generated by Django 4.1.4 on 2023-03-23 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('declaration', '0008_alter_packagedeclaration_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagedeclaration',
            name='shop_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='packagedeclaration',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='declaration.packagestatus'),
        ),
        migrations.AlterField(
            model_name='packagedeclaration',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
