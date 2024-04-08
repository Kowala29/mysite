from django.urls import path
from .views import list_filmes, new_filmes, \
    update_filmes, delete_filmes, new_genero

app_name = 'filme'

urlpatterns = [
    path('list_filmes/', list_filmes, name='list_filmes'),
    path('new_filmes/', new_filmes, name='new_filmes'),
    path('new_genero/', new_genero, name='new_genero'),
    path('update_filmes/<int:pk>/', update_filmes, name='update_filmes'),
    path('delete_filmes/<int:pk>/', delete_filmes, name='delete_filmes'),
]