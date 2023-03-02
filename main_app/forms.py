from django.forms import ModelForm
from .models import Painting

class PaintingForm(ModelForm):
    class Meta:
        model = Painting
        fields = ['date', 'painting_status']