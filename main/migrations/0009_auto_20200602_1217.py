# Generated by Django 3.0.6 on 2020-06-02 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_bookmark_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка на привью'),
        ),
        migrations.AlterField(
            model_name='article',
            name='color',
            field=models.CharField(blank=True, choices=[('b', 'Черный'), ('w', 'Белый')], max_length=1, null=True, verbose_name='Цвет картинки'),
        ),
        migrations.AlterField(
            model_name='article',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Article', to='main.Subject', verbose_name='Тематика'),
        ),
        migrations.AlterField(
            model_name='article',
            name='template_path',
            field=models.FilePathField(match='.html$', path='/run/media/roman/E (other)/Stock_of_articles/Stock-of-article/main/templates/main', verbose_name='Путь-к-шаблону-верстки'),
        ),
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.IntegerField(blank=True, editable=False, null=True, verbose_name='Просмотры'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BookmarkArticle', to='main.Article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BookmarkUser', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='dislike',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ArticleDislike', to='main.Article', verbose_name='Запись'),
        ),
        migrations.AlterField(
            model_name='dislike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Dislikes', to=settings.AUTH_USER_MODEL, verbose_name='Дизлайкнувший'),
        ),
        migrations.AlterField(
            model_name='like',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ArticleLike', to='main.Article', verbose_name='Запись'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Likes', to=settings.AUTH_USER_MODEL, verbose_name='Лайкнувший'),
        ),
        migrations.AlterField(
            model_name='likereview',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Review', to='main.Review', verbose_name='Коммент'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Notification', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='review',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Review', to='main.Article', verbose_name='Статья'),
        ),
        migrations.AlterField(
            model_name='review',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ReviewParent', to='main.Review', verbose_name='Родитель'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(max_length=5000, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ReviewUser', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
