from django.db import models

class Usuario(models.Model):
    email = models.EmailField(max_length=255, default='')
    username = models.CharField(max_length=30)
    senha = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.username
    
class Publicacoes(models.Model):
    dataPublicacao = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(default=0)
    comentarios = models.IntegerField(default=0)
    autorPub = models.ForeignKey(Usuario, on_delete=models.CASCADE)