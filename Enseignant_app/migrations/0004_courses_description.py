# Generated by Django 3.1.2 on 2022-04-17 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enseignant_app', '0003_homework_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='description',
            field=models.CharField(default=0, max_length=255),
        ),
    ]