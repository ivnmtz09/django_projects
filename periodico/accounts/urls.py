from django.urls import path
from .views import login_view, list_news, create_news

urlpatterns = [
    path('login/', login_view, name='login'),
    path('list/', list_news, name='list_news'),
    path('form/', create_news, name='create_news'),
]
