# Generated by Django 3.0.6 on 2020-05-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_auto_20200516_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
