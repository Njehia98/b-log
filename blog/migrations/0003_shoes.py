# Generated by Django 4.2.4 on 2023-12-04 13:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_cloth"),
    ]

    operations = [
        migrations.CreateModel(
            name="Shoes",
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
                ("size", models.IntegerField()),
            ],
        ),
    ]
