# Generated by Django 2.2.1 on 2019-12-31 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='favorita',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
