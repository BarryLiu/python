# Generated by Django 2.0.4 on 2018-08-06 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=32),
        ),
    ]
