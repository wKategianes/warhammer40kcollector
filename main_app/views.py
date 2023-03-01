from django.shortcuts import render
from .models import Model


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Add new view
def models_index(request):
    models = Model.objects.all()
    # We pass data to a template
    return render(request, 'models/index.html', {
        'models': models
    })

def models_detail(request, model_id):
    model = Model.objects.get(id=model_id)
    return render(request, 'models/detail.html', {'model': model})
