# Generated by Django 3.0.6 on 2020-06-02 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200602_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likereview',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LikeReview', to='main.Review', verbose_name='Коммент'),
        ),
    ]
