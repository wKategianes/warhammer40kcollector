from django.db import models

# Create your models here.
class Model(models.Model):
    name = models.CharField(max_length=100)
    faction = models.CharField(max_length=100)
    type = models.CharField(max_length=100)



# Changing this instance method
# does nto impact the database, therefore
# no makemigrations is necessary
def __str__(self):
    return f'{self.name} ({self.id})'