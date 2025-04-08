from django.contrib import admin

from secret.models import Secret, Log


@admin.register(Secret)
class SecretAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ("action", "name_secret")
