from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import *

router = DefaultRouter()
router.register('eleve', EleveViewset, basename='eleve')

urlpatterns = [
    path('/eleves/data', EleveViewset.as_view({'get' : 'getEleve'}), name='getEleve'),
]

urlpatterns += router.urls
