# Generated by Django 5.2.2 on 2025-06-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='source',
            field=models.CharField(choices=[('admin', 'Admin'), ('tmdb', 'TMDb')], default='admin', max_length=10),
        ),
    ]
