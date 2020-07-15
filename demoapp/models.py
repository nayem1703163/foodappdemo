from django.db import models

class Restaurants (models.Model):
    resname = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    
    def __str__(self):
        return self.resname
    

