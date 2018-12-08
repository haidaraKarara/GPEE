from django.contrib import admin
from datetime import date
from .models import *

class EleveAdmin(admin.ModelAdmin):
    list_display   = ('nom', 'prenom', 'adresse','classe','calculate_age',)
    list_filter    = ('sexe','classe')
    ordering       = ('date_arrivee',)
    search_fields  = ('nom','prenom')

    def calculate_age(self,eleve):
        """ 
        Retourne l'age de l'eleve 
        """
        today = date.today()
        return today.year - eleve.date_naissance.year - ((today.month, today.day) < (eleve.date_naissance.month, eleve.date_naissance.day))
    # En-tête de notre colonne
    calculate_age.short_description = 'Age'

    fieldsets = (
    # Fieldset 1 : meta-info (titre, auteur…)
    ('Général', {
        'classes': ['collapse',],
        'fields': ('nom', 'prenom', 'date_naissance','lieu_naissance','sexe','classe')
    }),
        # Fieldset 2 : informations secondaires
    ('Informations secondaires', {
        'classes': ['collapse',],
        'fields': ('tuteur','telephone','adresse','ancienne_ecole',)
    }),
    )

class ClasseAdmin(admin.ModelAdmin):
    list_display   = ('libelle',)
    search_fields  = ('libelle',)

# class TuteurAdmin(admin.ModelAdmin):
#     list_display   = ('nom','prenom','adresse','profession', 'telephone',)
#     list_filter    = ('profession',)
#     search_fields  = ('profession','telephone')

class MensualiteAdmin(admin.ModelAdmin):
    list_display   = ('has_paid', 'mois_paye', 'date_paye','eleve')
    list_filter    = ('mois_paye',)
    ordering       = ('mois_paye',)
    search_fields  = ('mois_paye','eleve')

admin.site.register(Eleve,EleveAdmin)
admin.site.register(Classe,ClasseAdmin)
# admin.site.register(Tuteur,TuteurAdmin)
admin.site.register(Mensualite,MensualiteAdmin)