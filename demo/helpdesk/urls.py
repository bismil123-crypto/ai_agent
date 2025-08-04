from django.urls import path
from .views import*
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('api/ask/', views.ask_question, name='ask_question'),
    path('detail/', views.detail, name='detail'),
    path('main/', views.main, name='main'),  # Redirect to home for main
]
