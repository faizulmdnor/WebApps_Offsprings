from django.urls import path
from . import views

urlpatterns = [
    path('prestasi/', views.prestasi, name='persons'),
]