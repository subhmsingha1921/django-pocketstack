# Generated by Django 3.1.7 on 2021-03-15 08:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('answers', '0002_auto_20210306_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='users_downvote',
            field=models.ManyToManyField(blank=True, related_name='answer_downvotes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='users_upvote',
            field=models.ManyToManyField(blank=True, related_name='answer_upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
