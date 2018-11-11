from django.conf.urls import url, include

from rest_framework import routers

from .viewsets import TreeViewSet

router = routers.DefaultRouter()
router.register(r'trees', TreeViewSet, base_name='tree')

urlpatterns = [
    url(r'^', include(router.urls)),
]
