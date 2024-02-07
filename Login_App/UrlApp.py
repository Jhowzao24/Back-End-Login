from django.urls import path, include
from .views import UserViews, LayoutInit
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('UserView', UserViews, basename='UserView')

urlpatterns = [
    path('Urls/', include(router.urls)),
    path('', LayoutInit),
]