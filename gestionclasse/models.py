from django.db import models
from datetime import date

class Classe(models.Model):
    libelle = models.CharField("Nom de la classe",max_length=100)

    def __str__(self):
        return self.libelle

class Eleve(models.Model):
    SEXE_CHOICES = (
        ('F', 'Femme'),
        ('H', 'Homme'),
    )
    def calculate_age(self,born):
        """ Calculate the age of the student """
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    tuteur = models.CharField("Son/Sa tuteur/tutrice",max_length=100,default='Aucun')
    telephone = models.IntegerField("Téléphone du tuteur",blank=True,null=True,unique=True)
    date_naissance = models.DateField("Date de naissance")
    lieu_naissance = models.CharField("Lieu de naissance",max_length=100)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    # AGE = calculate_age(date_naissance) # we calculate his age
    # age = models.IntegerField(default=calculate_age(date_naissance.value),blank=True)
    date_arrivee = models.DateField("Date d'arrivée",auto_now_add=True)
    ancienne_ecole = models.CharField("Ancienne école",max_length=100,blank=True,null=True,default='-')
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE,related_name='eleves')

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
        ('aout', 'août'),
        ('septembre', 'septembre'),
        ('octobre', 'octobre'),
        ('novembre', 'novembre'),
        ('decembre', 'decembre'),
    )
    has_paid = models.BooleanField(default=False)
    mois_paye = models.CharField("Mois payé",choices=MONTH_CHOICES,max_length=30)
    date_paye = models.DateField("Date paiment",auto_now_add=True)
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE,related_name='mensualite')

    class Meta:
        verbose_name = "Mensualité"
        ordering = ['date_paye']

    def __str__(self):
        return self.mois_paye


