# Generated by Django 3.0.5 on 2021-09-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210922_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientforrecipe',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
    ]
