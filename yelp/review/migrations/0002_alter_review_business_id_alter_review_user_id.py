# Generated by Django 4.1.2 on 2022-10-08 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("business", "0003_alter_business_attributes_alter_business_hours"),
        ("user", "0004_alter_yelpuser_compliment_cool_and_more"),
        ("review", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="business_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="business.business",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="user_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user.yelpuser",
            ),
        ),
    ]
