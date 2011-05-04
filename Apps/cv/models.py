from django.db import models
from django.forms import ModelForm
import datetime

class Info (models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    rue = models.CharField(max_length=200)
    cpostal = models.CharField(max_length=10)
    ville = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    #pic  = models.ImageField()
    
    def __unicode__(self):
        return self.nom

class Naissance(models.Model):
    info = models.ForeignKey(Info)
    date = models.DateTimeField(blank=False)
    
    def __unicode__(self):
        return self.date
    
    
class Experience(models.Model):
    info = models.ForeignKey(Info)
    noment = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    Des = models.TextField(max_length=500)
    dated = models.DateTimeField(blank=False)
    datef = models.DateTimeField('en cours')
    
    def __unicode__(self):
        return self.noment
        
class Diplome(models.Model):
    info = models.ForeignKey(Info)
    dip = models.CharField(max_length=100)
    date = models.CharField(max_length=5)
    
    def __unicode__(self):
        return self.dip
        
class Formation(models.Model):
    info = models.ForeignKey(Info)
    ecole = models.CharField(max_length=100)
    pays = models.CharField(max_length=50)
    dated = models.DateTimeField(blank=False)
    datef = models.DateTimeField('en cours')
    
    def __unicode__(self):
        return self.ecole

class Competence(models.Model):
    info = models.ForeignKey(Info)
    sort = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.sort
        
class Compdes(models.Model):
    sort = models.ForeignKey(Competence)
    desc = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.desc
    
    
    
    

    