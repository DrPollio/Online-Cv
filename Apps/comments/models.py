from django.db import models
from Apps.cv.models import Info 
from django.forms import ModelForm

class Commentaires(models.Model):
    noma = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    comment = models.TextField(max_length=800)
    info = models.ForeignKey(Info)
    