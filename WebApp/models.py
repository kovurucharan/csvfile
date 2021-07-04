from django.db import models

# Create your models here.
class Uploadfile(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(blank=True)
    Phone=models.IntegerField()

    def __str__(self):
        return self.Name