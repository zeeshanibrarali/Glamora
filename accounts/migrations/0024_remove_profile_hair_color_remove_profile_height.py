# Generated by Django 5.1.4 on 2025-04-03 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0023_alter_profile_budget_range_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="hair_color",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="height",
        ),
    ]
