from django.db import models

# Create your models here.


class Text(models.Model):
    descrizione=models.CharField(max_length=250)
    testo=models.TextField()
    def __str__(self):
        return self.descrizione