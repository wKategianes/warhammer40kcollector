from django.shortcuts import render, redirect
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
    # first, create a list of paint ids that the model DOES have
    id_list = model.paints.all().values_list('id')
      # query for the toys that the cat doesn't have
    # by using the exclude() method vs. the filter()
    paints_model_doesnt_have = Paint.objects.exclude(id__in=id_list)
    # instantiate PaintingForm to be rendered in the template
    painting_form = PaintingForm()
    return render(request, 'models/detail.html', {
    'model': model, 'painting_form': painting_form,
    'paints': paints_model_doesnt_have,
    })

class ModelCreate(CreateView):
    model = Model
    fields = ['name', 'faction', 'type']

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

def assoc_toy(request, model_id, paint_id):
    Model.objects.get(id=model_id).paints.add(paint_id)
    return redirect('detail', model_id=model_id)