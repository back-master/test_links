from django.apps import AppConfig


class ShorterConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.shorter"
    verbose_name = "Сократитель ссылок"
