from django.urls import path

from . import views

app_name = 'chatbot'
urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
    path('limparhistorico/', views.limpar_historico, name='limpar_historico'),
]
