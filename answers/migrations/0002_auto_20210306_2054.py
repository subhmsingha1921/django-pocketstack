# Generated by Django 3.1.7 on 2021-03-06 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
