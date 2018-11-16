from django.urls import include, path

from rest_framework import routers

from .viewsets import TreeViewSet

router = routers.DefaultRouter()
router.register(r'trees', TreeViewSet, base_name='tree')

urlpatterns = [
    path('', include(router.urls)),
]
