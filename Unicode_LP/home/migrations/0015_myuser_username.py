# Generated by Django 4.1.1 on 2022-11-03 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_myuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='username',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
