# Generated by Django 3.0.7 on 2020-08-08 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_auto_20200808_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='name',
            field=models.CharField(default='room', max_length=30),
        ),
    ]
