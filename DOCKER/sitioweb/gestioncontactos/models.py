from django.db import models

# Create your models here.

class Contacto(models.Model):
    id = models.AutoField(primary_key = True)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    Ncelular=models.IntegerField()
    fotogragia=models.ImageField(upload_to='albums/images/', blank=True, null=True)
    correo=models.EmailField()
    class Meta:
        unique_together = ('Ncelular',)

class Car(models.Model):
    name = models.CharField()
    color = models.CharField()
    description = models.TextField()
    type = models.IntegerField(choices=[
        (1, "Sedan"),
        (2, "Truck"),
        (4, "SUV"),
    ])