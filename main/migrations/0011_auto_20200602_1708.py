# Generated by Django 3.0.6 on 2020-06-02 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20200602_1218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmark',
            options={'ordering': ['-published']},
        ),
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-published']},
        ),
    ]
