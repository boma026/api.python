from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet

router = DefaultRouter()
router.register(r'Livros', LivroViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]