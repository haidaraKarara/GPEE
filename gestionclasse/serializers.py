from rest_framework import serializers
from .models import *

class MensualiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mensualite
        fields = ('has_paid','mois_paye','date_paye')

class EleveMensualiteSerializer(serializers.ModelSerializer):
    mensualites = MensualiteSerializer(many=True)
    class Meta:
        model = Eleve
        fields = ('id','nom','prenom','date_naissance','lieu_naissance','ancienne_ecole','mensualites')

class EleveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Eleve
        fields = '__all__'

    def create(self, validated_data):
        classe_data = validated_data.pop('classe')
        #classe = Classe.objects.create('',**classe_data)
        eleve = Eleve.objects.create(classe=classe_data, **validated_data)
        return eleve


class ClasseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Classe
        fields = '__all__'

class ClasseEleveMensualiteSerializer(serializers.ModelSerializer):
    eleves = EleveMensualiteSerializer(many=True)
    
    class Meta:
        model = Classe
        fields = ('id','libelle','eleves')

class StatSerializer(serializers.Serializer):
    nb_of_students = serializers.IntegerField()
    nb_of_class = serializers.IntegerField()
    nb_of_boys = serializers.IntegerField()
    nb_of_girls = serializers.IntegerField()

    class Meta:
        model = Classe
        fields = '__all__'
