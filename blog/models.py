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