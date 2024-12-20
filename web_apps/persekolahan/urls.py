from django.urls import path
from . import views

urlpatterns = [
    path('persekolahan/', views.persekolahan, name='persons'),
]