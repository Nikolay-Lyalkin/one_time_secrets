import random
import string


def generate_secret_key():
    """Генерация кода доступа из 9 знаков"""

    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choices(characters, k=9))


def get_client_ip(request):
    """Получение IP адреса клиента"""

    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
