from django.db import models

# Create your models here.
class Decade(models.Model):
    start_year = models.CharField(max_length=100)

    def __str__(self):
        return self.start_year

class Fad(models.Model):
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='fads')
    name = models.CharField(max_length=100, default='no fad name')
    description = models.CharField(max_length=200, default='no description')
    image_url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name