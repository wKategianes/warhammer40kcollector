from django.db import models
from django.urls import reverse

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

def get_absolute_url(self):
    return reverse('detail', kwargs={'model_id': self.id})

PAINT = (
    ('P', 'Primed'),
    ('D', 'Detailed'),
    ('C', 'Completed'),
)

class Painting(models.Model):
    date = models.DateField('Painted Date')
    painting_status = models.CharField(
        max_length=1,
        choices=PAINT,
        default=PAINT[0][0]
    )

    # Create a model_id FK
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_painting_status_display()} on {self.date}"

class Meta:
    ordering = ['-date']

# Create your models here.
class Paint(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('paints_detail', kwargs={'pk': self.id})