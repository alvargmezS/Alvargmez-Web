from django.db import models

# Create your models her

class tecnologia(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']

class proyecto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    url_codigo = models.URLField(unique=True, blank=True, null=True)
    url_demo = models.URLField(unique=True, blank=True, null=True)
    tecnologias = models.ManyToManyField(tecnologia, blank=True)
    icono = models.CharField(max_length=50, default='fa-server')

    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ['-fecha']