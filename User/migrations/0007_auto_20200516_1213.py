# Generated by Django 3.0.6 on 2020-05-16 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200514_1548'),
        ('User', '0006_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='main.Subject'),
        ),
    ]
