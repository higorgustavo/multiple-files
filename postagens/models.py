from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_post = models.DateTimeField(auto_now_add=True, verbose_name='Data de postagem')

    def __str__(self):
        return self.titulo


class Arquivo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='arquivos_post', null=True, blank=True)

    def __str__(self):
        # return self.post.titulo + " - " + str(self.arquivo)
        return str(self.arquivo)

    def delete(self, *args, **kwargs):
        self.arquivo.delete()
        super().delete(*args, **kwargs)
