from django.db import models

# Create your models here.
class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    identifier = models.CharField(max_length=20,unique=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        ordering = ['name']

    def __str__(self):
        return self.name