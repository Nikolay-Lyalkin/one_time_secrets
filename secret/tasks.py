from celery import shared_task
from django.utils import timezone

from secret.models import Secret


@shared_task
def checking_secrets():

    for secret in Secret.objects.all():
        if not secret.is_active:
            secret.delete()
        if secret.ttl_seconds:
            if secret.created_at + timezone.timedelta(seconds=secret.ttl_seconds) < timezone.now():
                secret.delete()
