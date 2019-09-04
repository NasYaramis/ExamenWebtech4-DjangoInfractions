from django.urls import path
from . import views

app_name = 'compinfractions'

urlpatterns = [
    path('', views.index, name='index'),
    path('infractions/<int:infractions_speed>', views.search, name='search'),
]
