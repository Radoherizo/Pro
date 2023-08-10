from django.http import HttpResponse, request
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import *
from .serializers import *


class EleveViewset(viewsets.ModelViewSet):
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer

    def getEleve(self):
        nom = request.data.get('nom')

        print(nom)
