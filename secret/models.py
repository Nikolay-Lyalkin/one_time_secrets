from django.db import models


class Secret(models.Model):
    name = models.CharField(verbose_name="Наименование секрета", max_length=100,  blank=True, null=True)
    secret = models.TextField(verbose_name="Секрет", max_length=1000)
    passphrase = models.TextField(verbose_name="Пароль для дополнительной защиты", max_length=100, blank=True, null=True)
    ttl_seconds = models.PositiveIntegerField(verbose_name="Время жизни (секунды)", blank=True, null=True)
    is_active = models.BooleanField(verbose_name="Активность секрета", default=True)
    created_at = models.DateTimeField(verbose_name="Дата публикации", auto_now_add=True)
    secret_key = models.CharField(verbose_name="Код доступа", max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Секрет"
        verbose_name_plural = "Секреты"
        db_table = "secrets"


class Log(models.Model):

    action = models.CharField(verbose_name="Действие пользователя", max_length=100,  blank=True, null=True)
    name_secret = models.CharField(verbose_name="Наименование секрета", max_length=100,  blank=True, null=True)
    secret = models.TextField(verbose_name="Секрет", max_length=1000, blank=True, null=True)
    ttl_seconds = models.CharField(verbose_name="Время хранения секрета", max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="Дата публикации", auto_now_add=True)
    secret_key = models.CharField(verbose_name="Код доступа", max_length=100, blank=True, null=True)
    ip = models.CharField(verbose_name="IP адрес", max_length=100,  blank=True, null=True)

    def __str__(self):
        return f"{self.action} - {self.name_secret}"

    class Meta:
        verbose_name = "Лог"
        verbose_name_plural = "Логи"
        db_table = "log"
