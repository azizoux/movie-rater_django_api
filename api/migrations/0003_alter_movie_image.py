# Generated by Django 4.1.2 on 2022-10-29 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_movie_liked_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]