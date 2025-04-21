import string
import random

from django.db import models

from config.settings import MAIN_HOST


class Link(models.Model):
    url = models.URLField("Оригинальный URL ссылки")
    token = models.CharField("Токен", max_length=6, unique=True, db_index=True)

    link_count = models.PositiveIntegerField("Кол-во переходов", default=0)

    class Meta:
        verbose_name = "ссылку"
        verbose_name_plural = "Ссылки"

    def __str__(self):
        return f"{self.url}"

    def save(self, *args, **kwargs):
        if not self.token:
            while True:
                token = self.generate_token()
                if not Link.objects.filter(token=token).exists():
                    self.token = token
                    break
        super().save(*args, **kwargs)

    @property
    def reversed_url(self):
        return f"{MAIN_HOST}/api/v1/link/{self.token}/"

    @staticmethod
    def generate_token(length=6):
        chars = string.ascii_letters + string.digits
        return "".join(random.choices(chars, k=length))
