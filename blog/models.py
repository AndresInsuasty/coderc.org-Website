from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name="Titulo")
    description = models.TextField(verbose_name="Contenido" )
    image = models.ImageField(verbose_name="Imagen",upload_to="blog", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ['-created']

    def _str_(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments',null=True, blank=True)
    author = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['-created_date']

    def __str__(self):
        return self.text