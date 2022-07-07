from django.db import models

# Create your models here.

class Articulos(models.Model):
    name=models.CharField(max_length=50)
    maker_website=models.URLField(max_length=100)
    made_at=models.PositiveIntegerField()
