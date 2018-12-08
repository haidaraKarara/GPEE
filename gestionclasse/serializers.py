from rest_framework import serializers
from .models import *

class MensualiteSerializer(serializers.ModelSerializer):

    class Meta:
        models = Mensualite
        fields = '__all__'

class EleveSerializer(serializers.ModelSerializer):
    # mensualite = MensualiteSerializer(many=True)

    class Meta:
        model = Eleve
        fields = '__all__'


class ClasseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Classe
        fields = '__all__'

class ClasseEleveSerializer(serializers.ModelSerializer):
    eleves = EleveSerializer(many=True)
    
    class Meta:
        model = Classe
        fields = ('id','libelle','eleves')
