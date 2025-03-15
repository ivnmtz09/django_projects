from django.urls import path
from .views import NoticiaListCreateView, NoticiaDetailView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('noticias/', NoticiaListCreateView.as_view(), name='noticia-list'),
    path('noticias/<int:pk>/', NoticiaDetailView.as_view(), name='noticia-detail'),
]
