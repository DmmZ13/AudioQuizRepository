from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'classes'
urlpatterns = [
    path('', views.ClasseListView.as_view(), name='index'),
    path('<int:pk>/', views.ClasseMuralView.as_view(), name='mural'),
    path('<int:pk>/atividades', views.ClasseAtividadesView.as_view(), name='atividades_index'),
    path('<int:pk>/atividades/upload', views.AtividadeCreateView.as_view(), name='atividades_create'),
    path('<int:pk>/flashcards', views.ClasseFlashcardsView.as_view(), name='flashcards'),
    path('<int:pk>/create_flashcards', views.ClasseFlashcardsCreate.as_view(), name='create_flashcards'),
    path('create/', views.ClasseCreateView.as_view(), name='create'),
    path('<int:pk>/mensagem/', views.MensagemCreateView.as_view(), name='mensagem'),
    path('<int:pk>/mensagem/delete/<int:mensagem_id>/', views.MensagemDeleteView.as_view(), name='delete_message'),
    path('delete/<int:pk>/', views.ClasseDeleteView.as_view(), name='delete'),
    path('download/<int:pk>/', views.download_pdf, name='download_pdf'),
    path('aceitar_convite/<int:notificacao_id>/', views.aceitar_convite, name='aceitar_convite'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
