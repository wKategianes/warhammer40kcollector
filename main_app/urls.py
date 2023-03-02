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
    path('paints/', views.PaintList.as_view(), name='paints_index'),
    path('paints/<int:pk>/', views.PaintDetail.as_view(), name='paints_detail'),
    path('paints/create/', views.PaintCreate.as_view(), name='paints_create'),
    path('paints/<int:pk>/update/', views.PaintUpdate.as_view(), name='paints_update'),
    path('paints/<int:pk>/delete/', views.PaintDelete.as_view(), name='paints_delete'),
]