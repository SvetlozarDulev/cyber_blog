from django.urls import path
from .views import encryption

urlpatterns = [
    path('', encryption, name='encrypt_text')
]