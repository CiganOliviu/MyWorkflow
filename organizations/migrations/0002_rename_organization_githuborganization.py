# Generated by Django 3.2.5 on 2021-07-07 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Organization',
            new_name='GithubOrganization',
        ),
    ]
