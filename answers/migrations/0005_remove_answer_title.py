# Generated by Django 3.1.7 on 2021-03-16 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0004_remove_answer_is_accepted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='title',
        ),
    ]