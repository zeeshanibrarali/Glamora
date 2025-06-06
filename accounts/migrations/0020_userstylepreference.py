# Generated by Django 5.1.4 on 2025-04-01 08:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0019_cart_stripe_checkout_session_id_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserStylePreference",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("clothing_types", models.CharField(max_length=100)),
                ("height", models.CharField(max_length=50)),
                ("body_shape", models.CharField(max_length=100)),
                ("skin_tone", models.CharField(max_length=100)),
                ("hair_color", models.CharField(max_length=50)),
                ("clothing_size", models.CharField(max_length=10)),
                (
                    "favorite_brands",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("budget_range", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
