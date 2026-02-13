from django.urls import path
from .views import predict   # ✅ correct function name

urlpatterns = [
    path('', predict, name='predict'),
]