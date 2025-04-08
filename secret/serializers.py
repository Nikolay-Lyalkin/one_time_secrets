from rest_framework.serializers import ModelSerializer

from secret.models import Secret


class SecretSerializer(ModelSerializer):

    class Meta:
        model = Secret
        fields = ["name", "secret", "passphrase", "ttl_seconds", "created_at"]
