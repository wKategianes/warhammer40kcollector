from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Model, Paint
from .forms import PaintingForm


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
    # instantiate PaintingForm to be rendered in the template
    painting_form = PaintingForm()
    return render(request, 'models/detail.html', {'model': model, 'painting_form': painting_form})

class ModelCreate(CreateView):
    model = Model
    field = '__all__'

class ModelUpdate(UpdateView):
    model = Model
    fields = ['faction', 'type']

class ModelDelete(DeleteView):
    model = Model
    success_url = '/models'

class PaintList(ListView):
  model = Paint

class PaintDetail(DetailView):
  model = Paint

class PaintCreate(CreateView):
  model = Paint
  fields = '__all__'

class PaintUpdate(UpdateView):
  model = Paint
  fields = ['name', 'color']

class PaintDelete(DeleteView):
  model = Paint
  success_url = '/paints'