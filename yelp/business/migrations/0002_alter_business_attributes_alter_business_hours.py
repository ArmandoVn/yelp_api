# Generated by Django 4.1.2 on 2022-10-07 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='attributes',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='business',
            name='hours',
            field=models.JSONField(default=dict),
        ),
    ]