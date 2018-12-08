from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAdminUser

class ClasseList(generics.ListAPIView):
    """ Used for read-only endpoints to represent a collection of model instances. """
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
    permission_classes = (IsAdminUser,)

class ClasseEleveList(generics.RetrieveAPIView):
    """ Used for read-only endpoints to represent a single model instance. """
    queryset = Classe.objects.all()
    serializer_class = ClasseEleveSerializer
    permission_classes = (IsAdminUser,)

class CreateEleve(generics.CreateAPIView):
    """ Used for create-only endpoints. """
    queryset = Eleve.objects.all()
    serializer_class = EleveSerializer
    permission_classes = (IsAdminUser,)
