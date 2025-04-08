from django.core.cache import cache
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import generics
from rest_framework.response import Response

from secret.models import Secret, Log
from secret.serializers import SecretSerializer
from secret.services import generate_secret_key, get_client_ip


class SecretCreateAPIView(generics.CreateAPIView):
    serializer_class = SecretSerializer

    def create(self, request, *args, **kwargs):
        """Создание секрета"""

        data = cache.get(request.data["name"])

        if not data:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            new_secret = serializer.save()
            new_secret.secret = urlsafe_base64_encode(force_bytes(new_secret.secret))  # Кодирование секрета
            gen_secret_key = generate_secret_key()
            new_secret.secret_key = gen_secret_key
            new_secret.save()
            message = "Код доступа к секрету"

            cache.set(request.data["name"], gen_secret_key, 60 * 5)  # Кэширование на 5 минут созданного объекта

            ip = get_client_ip(request)  # Получение IP адреса пользователя
            Log.objects.create(action="Создание секрета", name_secret=new_secret.name, secret=new_secret.secret, ttl_seconds=new_secret.ttl_seconds, secret_key=new_secret.secret_key, ip=ip)

            return Response({'message': message, 'secret_key': gen_secret_key}, headers=self._get_no_cache_headers())

        message = "Код доступа к секрету"
        return Response({'message': message, 'secret_key': data})

    def _get_no_cache_headers(self):
        return {
            'Cache-Control': 'no-store',
            'Pragma': 'no-cache',
            'Expires': '0',
        }


class SecretGetAPIView(generics.ListAPIView):
    queryset = Secret.objects.all()
    serializer_class = SecretSerializer

    def get(self, request, secret_key, *args, **kwargs):
        """Просмотр секрета"""

        ip = get_client_ip(request)
        secret_obj = Secret.objects.filter(secret_key=secret_key).first()

        if secret_obj and secret_obj.is_active:
            secret_obj.is_active = False
            secret = urlsafe_base64_decode(secret_obj.secret).decode("utf-8")
            secret_obj.save()
            message = "Ваш секрет"
            Log.objects.create(action="Просмотр секрета", name_secret=secret_obj.name, secret=secret_obj.secret,
                               ttl_seconds=secret_obj.ttl_seconds, secret_key=secret_obj.secret_key, ip=ip)
            return Response({"message": message, "secret": secret})
        else:
            message = "По вашему ключу доступа ничего не найдено"
            return Response({"message": message})


class SecretDeleteAPIView(generics.RetrieveAPIView):

    def delete(self, request, secret_key, *args, **kwargs):
        """Удаление секрета"""

        ip = get_client_ip(request)
        secret = Secret.objects.get(secret_key=secret_key)
        if secret:
            Log.objects.create(action="Удаление секрета", name_secret=secret.name, secret=secret.secret,
                               ttl_seconds=secret.ttl_seconds, secret_key=secret.secret_key, ip=ip)
            secret.delete()
            message = "Секрет успешно удалён"
            return Response({"message": message})
        else:
            message = "Секрет по данному ключу не найден"
            return Response({"message": message})
