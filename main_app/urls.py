from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('models/', views.models_index, name='index'),
    path('models/<int:model_id>/', views.models_detail, name='detail'),
]