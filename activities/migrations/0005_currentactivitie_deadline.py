# Generated by Django 3.2.5 on 2021-07-07 20:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_currentactivitie_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentactivitie',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
