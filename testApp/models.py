from django.db import models
from django.conf import settings
from django.utils import timezone

class Pagina1(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    text = models.TextField()
    fechaCreacion = models.DateTimeField(default=timezone.now)
    fechaPubli = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fechaPubli = timezone.now()
        self.save

    def __str__(self):
        return self.titulo