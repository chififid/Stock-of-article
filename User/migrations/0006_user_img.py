# Generated by Django 3.0.6 on 2020-05-10 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_auto_20200510_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='аватарка'),
        ),
    ]
