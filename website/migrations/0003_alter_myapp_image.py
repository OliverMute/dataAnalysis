# Generated by Django 3.2.9 on 2021-11-25 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_myapp_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myapp',
            name='image',
            field=models.ImageField(upload_to='my_apps'),
        ),
    ]
