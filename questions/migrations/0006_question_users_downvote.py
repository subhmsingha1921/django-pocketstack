# Generated by Django 3.1.7 on 2021-03-13 09:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0005_auto_20210311_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='users_downvote',
            field=models.ManyToManyField(blank=True, related_name='question_downvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
