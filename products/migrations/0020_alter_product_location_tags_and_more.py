# Generated by Django 5.1.4 on 2025-04-03 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0019_alter_product_body_shapes_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="location_tags",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="product",
            name="occasion_tags",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="product",
            name="seasonal_tags",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
