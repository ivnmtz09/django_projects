from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, default= "Tegnologia")
    ciudad  = models.CharField(max_length=20, default="Riohacha")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
