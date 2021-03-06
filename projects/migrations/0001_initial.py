# Generated by Django 3.2.5 on 2021-07-03 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevelopmentStack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=50)),
                ('details', models.TextField(default='None')),
                ('github_url', models.URLField(default='None')),
                ('future_development_notes', models.TextField(default='None')),
                ('stack', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='projects.developmentstack')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('details', models.TextField()),
                ('github_url', models.URLField()),
                ('start_date', models.DateTimeField()),
                ('importance_level', models.PositiveIntegerField(default=0)),
                ('project_visibility', models.CharField(choices=[('public', 'public'), ('private', 'private'), ('forked', 'forked')], default='public', max_length=25)),
                ('stack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.developmentstack')),
            ],
        ),
    ]
