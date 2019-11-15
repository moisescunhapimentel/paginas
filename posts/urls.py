from django.urls import path
from .views import ListagemView, PostagemDetailView, NovoPost, PostUpdateView, PostDeleteView
urlpatterns = [
    path('post/<int:pk>/', PostagemDetailView.as_view(), name='post_detail'),
    path('post/new/', NovoPost.as_view(), name='post_new'),
    path('', ListagemView.as_view(), name ='listagem'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post_delete'),
]