from django.urls import path

from secret import views

from .apps import SecretConfig

app_name = SecretConfig.name

urlpatterns = [
    # Advertisement
    path("secret/create/", views.SecretCreateAPIView.as_view(), name="secret_create"),
    path("secret/get/<str:secret_key>/", views.SecretGetAPIView.as_view(), name="secret_get"),
    path("secret/delete/<str:secret_key>/", views.SecretDeleteAPIView.as_view(), name="secret_get"),
]
