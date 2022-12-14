# Generated by Django 4.1.2 on 2022-10-08 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("business", "0003_alter_business_attributes_alter_business_hours"),
        ("user", "0004_alter_yelpuser_compliment_cool_and_more"),
        ("review", "0002_alter_review_business_id_alter_review_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="business_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
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
                related_name="reviews",
                to="user.yelpuser",
            ),
        ),
    ]
