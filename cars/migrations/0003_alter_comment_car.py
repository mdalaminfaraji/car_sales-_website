# Generated by Django 5.0 on 2023-12-31 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='cars.car'),
        ),
    ]
