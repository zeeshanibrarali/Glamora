# Generated by Django 5.1.4 on 2025-03-30 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0018_remove_profile_body_type_remove_profile_height_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="stripe_checkout_session_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="cart",
            name="stripe_payment_intent_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
