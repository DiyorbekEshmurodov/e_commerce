from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import ProductViewsSet,ReviewViewSet,CategoryViewSet

router = DefaultRouter()
router.register(r'product',ProductViewsSet)
router.register(r'reviews',ReviewViewSet)
router.register(r'categories',CategoryViewSet)

urlpatterns = [
    path('',include(router.urls))
]