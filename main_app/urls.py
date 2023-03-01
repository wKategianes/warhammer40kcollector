from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('models/', views.models_index, name='index'),
    path('models/<int:model_id>/', views.models_detail, name='detail'),
    path('models/create/', views.ModelCreate.as_view(), name='models_create'),
    path('models/<int:pk>/update', views.ModelUpdate.as_view(), name='models_update'),
    path('models/<int:pk>/delete', views.ModelDelete.as_view(), name='models_delete'),
]