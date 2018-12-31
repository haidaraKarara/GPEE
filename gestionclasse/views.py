from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND)
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.renderers import JSONRenderer



class ClassList(generics.ListAPIView):
    """ Used for read-only endpoints to represent a collection of model instances. """
    queryset = Classe.objects.all()
    serializer_class = ClasseSerializer
    permission_classes = (IsAdminUser,)

class ClasseEleveMensualiteList(generics.RetrieveAPIView):
    """ Used for read-only endpoints to represent a single model instance. """
    queryset = Classe.objects.all()
    serializer_class = ClasseEleveMensualiteSerializer
    permission_classes = (IsAdminUser,)

class SingleStudent(generics.RetrieveUpdateDestroyAPIView):
    """ Used for read-write-delete endpoints to represent a single model instance. """
    #queryset = Eleve.objects.all()
    serializer_class = EleveSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return Eleve.objects.filter(pk=self.kwargs['pk'])

class CreateStudent(generics.CreateAPIView):
    """ Used for create-only endpoints. """
    serializer_class = EleveSerializer
    permission_classes = (IsAdminUser,)

class DeleteStudent(generics.DestroyAPIView):
    """ Used for delete-only endpoints for a single model instance. """
    permission_classes = (IsAdminUser,)
    serializer_class = EleveSerializer

class CreateClass(generics.CreateAPIView):
    """ used for create-only endpoint """
    serializer_class = ClasseSerializer
    permission_classes = (IsAdminUser,)

class DeleteClass(generics.DestroyAPIView):
    """ Used for delete-only endpoints for a single model instance. """
    permission_classes = (IsAdminUser,)
    serializer_class = ClasseSerializer

class UpdateClass(generics.UpdateAPIView):
    """ Used for update-only endpoints for a single model instance. """
    permission_classes = (IsAdminUser,)
    serializer_class = ClasseSerializer
    
# View pour les statistiques
@api_view(["GET"])
@permission_classes((IsAdminUser,))
def statistics(request):
    """ API endpoint that allows users to get some statistics """
    nb_of_students = Eleve.objects.all().count()
    nb_of_class = Classe.objects.all().count()
    nb_of_boys = len(Eleve.objects.filter(Q(sexe='M')))
    nb_of_girls = len(Eleve.objects.filter(Q(sexe='F')))
    stat = Statistics(nb_of_students=nb_of_students,
                        nb_of_class=nb_of_class,
                        nb_of_boys=nb_of_boys,
                        nb_of_girls=nb_of_girls
                    )

    serializer = StatSerializer(stat)
    print(serializer)
    return Response(serializer.data,status=HTTP_200_OK)
                    