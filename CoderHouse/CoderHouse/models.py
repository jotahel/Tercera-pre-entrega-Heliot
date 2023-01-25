from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=200)

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField()
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField()
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
