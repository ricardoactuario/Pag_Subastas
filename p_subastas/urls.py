from django.urls import path
from . import views

urlpatterns = [
    path('ofertar/', views.ofertar, name='ofertar'),
]