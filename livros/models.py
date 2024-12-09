from django.db import models

class Livro(models.Model):
    name = models.CharField(max_length=50)
    ano = models.IntegerField(null=True)
    autor = models.CharField(max_length=50)

    def __str__(self):
        return self.name