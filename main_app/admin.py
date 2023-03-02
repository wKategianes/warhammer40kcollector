from django.contrib import admin
from .models import Model, Painting, Paint

# Register your models here.
admin.site.register(Model)
admin.site.register(Painting)
admin.site.register(Paint)