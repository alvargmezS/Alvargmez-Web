from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.

class cv(models.Model):
    archivo = models.FileField(
        upload_to='cv/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        help_text='Fichero PDF del currículum. Al subir uno nuevo se sustituye el anterior.',
    )
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Currículum Vitae'

    def save(self, *args, **kwargs):
        if self.pk:
            anterior = cv.objects.filter(pk=self.pk).first()
            if anterior and anterior.archivo and anterior.archivo != self.archivo:
                anterior.archivo.delete(save=False)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'CV'
        verbose_name_plural = 'CV'
