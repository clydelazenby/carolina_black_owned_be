# Generated by Django 4.2.5 on 2023-09-12 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_customuser_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='default_username', max_length=30, unique=True),
        ),
    ]
