from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    image1 = models.ImageField(verbose_name="Imagen",upload_to="comproagro", null=True, blank=True)
    image2 = models.ImageField(verbose_name="Imagen",upload_to="comproagro", null=True, blank=True)
    image3 =models.ImageField(verbose_name="Imagen",upload_to="comproagro", null=True, blank=True)
    description = models.TextField(verbose_name="Descripcion")
    phone = models.CharField(max_length=20,verbose_name="Telefono")
    email = models.CharField(max_length=40,verbose_name="Correo")
    address = models.CharField(max_length=100,verbose_name="Direccion")
    technic_field = models.FileField(verbose_name="Ficha Tecnica",upload_to="comproagro/fichatecnica",null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['-created']

    def _str_(self):
        return self.title