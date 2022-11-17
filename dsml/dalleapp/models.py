from django.db import models

# Create your models here.


class Text(models.Model):
    descrizione=models.CharField(max_length=250)
    testo=models.TextField()
    def __str__(self):
        return self.descrizione 

class Configuration(models.Model):
    summaryModel=models.CharField(max_length=250)
    openaiSessK=models.CharField(max_length=250)
    nImages=models.IntegerField()

    def __str__(self):
        return self.openaiSessK 