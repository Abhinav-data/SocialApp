# Generated by Django 3.0.2 on 2020-02-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_auto_20200203_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='content',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
