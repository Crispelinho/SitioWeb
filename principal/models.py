from django.db import models

# Create your models here.

class Contacto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    Ncelular=models.IntegerField()
    fotogragia=models.ImageField(upload_to='albums/images/')
    correo=models.EmailField(blank=True, null=True)
    class Meta:
        unique_together = ('Ncelular',)