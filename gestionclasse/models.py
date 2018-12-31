from django.db import models
from datetime import date

class Classe(models.Model):
    libelle = models.CharField("<Classe>",max_length=100,unique=True)

    def __str__(self):
        return self.libelle

    class Meta:
        ordering = ('libelle',)


class Eleve(models.Model):
    SEXE_CHOICES = (
        ('F', 'F'),
        ('M', 'M'),
    )
    # def calculate_age(self,born):
    #     """ Calculate the age of the student """
    #     today = date.today()
    #     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    date_naissance = models.DateField("Date de naissance")
    lieu_naissance = models.CharField("Lieu de naissance",max_length=100)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,related_name='eleves')
    tuteur = models.CharField("Son/Sa tuteur/tutrice",max_length=100,default='Aucun',blank=True)
    telephone = models.IntegerField("Téléphone du tuteur",blank=True,null=True)
    adresse = models.CharField(max_length=100,blank=True)
    ancienne_ecole = models.CharField("Ancienne école",max_length=100,blank=True,null=True,default='-')
    date_arrivee = models.DateField("Date d'arrivée",blank=True,null=True)

    def __str__(self):
        return self.prenom  +' '+ self.nom

    class Meta:
        verbose_name = "Élève"


class Mensualite(models.Model):
    MONTH_CHOICES = (
        ('janvier', 'janvier'),
        ('fevrier', 'février'),
        ('mars', 'mars'),
        ('avril', 'avril'),
        ('mai', 'mai'),
        ('juin', 'juin'),
        ('juillet', 'juillet'),
        # ('aout', 'août'),
        # ('septembre', 'septembre'),
        ('octobre', 'octobre'),
        ('novembre', 'novembre'),
        ('decembre', 'decembre'),
    )
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE,related_name='mensualites')
    has_paid = models.BooleanField(default=False)
    mois_paye = models.CharField("Mois payé",choices=MONTH_CHOICES,max_length=30)
    date_paye = models.DateField("Date paiment",auto_now_add=True,blank=True)

    class Meta:
        verbose_name = "Mensualité"
        ordering = ['date_paye']

    def __str__(self):
        return self.mois_paye

class Statistics(object):

    def __init__(self, nb_of_students, nb_of_class, nb_of_boys,nb_of_girls):
        self.nb_of_students = nb_of_students
        self.nb_of_class = nb_of_class
        self.nb_of_boys = nb_of_boys 
        self.nb_of_girls = nb_of_girls



