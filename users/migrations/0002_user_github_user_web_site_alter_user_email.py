# Generated by Django 4.2.4 on 2023-09-29 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='github',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='web_site',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
