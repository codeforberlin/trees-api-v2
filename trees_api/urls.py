from django.urls import include, path
from rest_framework import routers

from .viewsets import BoroughViewSet, GenusViewSet, SpeciesViewSet, TreeViewSet

router = routers.DefaultRouter()
router.register(r'trees', TreeViewSet, basename='tree')
router.register(r'species', SpeciesViewSet, basename='species')
router.register(r'genera', GenusViewSet, basename='genus')
router.register(r'boroughs', BoroughViewSet, basename='borough')

urlpatterns = [
    path('', include(router.urls)),
]
