# Generated by Django 3.0.2 on 2020-02-06 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0006_delete_friend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpost',
            name='user',
        ),
        migrations.AddField(
            model_name='userpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
