# Generated by Django 4.0.3 on 2022-05-04 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0007_alter_chatbot_reclamation_advertisement'),
    ]

    operations = [
        migrations.AddField(
            model_name='parents',
            name='kid_name2',
            field=models.CharField(default='Mhamdi', max_length=255),
        ),
    ]