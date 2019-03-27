from django.db import models


class EstadoComentario(models.Model):
    codigo = models.CharField(max_length=255, null=False, blank=True)
    nombre = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'EstadoComentario'
        verbose_name_plural = 'EstadosComentario'


class Comentario(models.Model):
    texto = models.TextField(null=False, blank=False)
    fecha_publicacion = models.DateTimeField(null=False, blank=True)
    perfil = models.ForeignKey('seguridades.Perfil', null=True, blank=True, on_delete=models.CASCADE)
    mascota = models.ForeignKey('mascotas.Mascota', null=False, blank=False, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoComentario, null=False, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
