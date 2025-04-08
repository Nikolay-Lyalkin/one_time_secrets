# Generated by Django 5.2 on 2025-04-08 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("secret", "0003_secret_is_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="Log",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "action",
                    models.CharField(blank=True, max_length=100, null=True, verbose_name="Действие пользователя"),
                ),
                (
                    "name_secret",
                    models.CharField(blank=True, max_length=100, null=True, verbose_name="Наименование секрета"),
                ),
                ("secret", models.TextField(blank=True, max_length=1000, null=True, verbose_name="Секрет")),
                (
                    "ttl_seconds",
                    models.CharField(blank=True, max_length=100, null=True, verbose_name="Время хранения секрета"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")),
                ("secret_key", models.CharField(blank=True, max_length=100, null=True, verbose_name="Код доступа")),
                ("ip", models.CharField(blank=True, max_length=100, null=True, verbose_name="IP адрес")),
            ],
            options={
                "verbose_name": "Лог",
                "verbose_name_plural": "Логи",
                "db_table": "log",
            },
        ),
    ]
