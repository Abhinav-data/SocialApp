# Generated by Django 3.0.2 on 2020-02-03 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20200203_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profilePic',
            field=models.ImageField(blank=True, default='profile_image/default.png', upload_to='profile_image/'),
        ),
    ]
