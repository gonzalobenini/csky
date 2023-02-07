from  django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='chessbe-base'),
    path('start/', views.get_pieces, name='chessbe-matchinit'),
    path('move/', views.get_move, name='chessbe-getmove')
]