# Generated by Django 5.2 on 2025-04-21 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Link",
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
                ("url", models.URLField(verbose_name="Оригинальный URL ссылки")),
                (
                    "token",
                    models.CharField(
                        db_index=True, max_length=6, unique=True, verbose_name="Токен"
                    ),
                ),
                (
                    "link_count",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Кол-во переходов"
                    ),
                ),
            ],
            options={
                "verbose_name": "ссылку",
                "verbose_name_plural": "Ссылки",
            },
        ),
    ]
