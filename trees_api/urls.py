from django.urls import include, path

from rest_framework import routers

from .viewsets import (
    TreeViewSet,
    SpeciesViewSet,
    GenusViewSet,
    BoroughViewSet
)

router = routers.DefaultRouter()
router.register(r'trees', TreeViewSet, base_name='tree')
router.register(r'species', SpeciesViewSet, base_name='species')
router.register(r'genera', GenusViewSet, base_name='genus')
router.register(r'boroughs', BoroughViewSet, base_name='borough')

urlpatterns = [
    path('', include(router.urls)),
]
