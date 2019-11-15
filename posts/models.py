from django.db import models
from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    autor = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    texto = models.TextField()

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('listagem')