from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_post, name='listar_post'),
    path('new/', novo_post, name='novo_post'),
    path('new2/', novo_post2, name='novo_post2'),
    path('detail/<int:id>/', detalhe_post, name='detalhe_post')
]