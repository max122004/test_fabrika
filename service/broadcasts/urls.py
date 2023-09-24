from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, BroadcastViewSet, MessageViewSet

router = DefaultRouter()
# клиенты
router.register(r'clients', ClientViewSet)
# рассылка
router.register(r'broadcasts', BroadcastViewSet)
# сообщения
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]