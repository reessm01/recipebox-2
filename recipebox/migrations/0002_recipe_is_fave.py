# Generated by Django 2.2.3 on 2019-08-21 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipebox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='is_fave',
            field=models.BooleanField(default=False),
        ),
    ]
