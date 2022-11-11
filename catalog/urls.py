# urls de nuestra aplicaciÃ³n catalogo
from django.urls import path
from .views import index, acerca_de, BookListView, BookDetailView, AuthorListView, AuthorDetailView

urlpatterns = [
    path('', index, name='index'),
    path('acercade/', acerca_de, name='acercade'),
    path('libros/', BookListView.as_view(), name='lista-libros'),
    path('libros/<int:pk>', BookDetailView.as_view(), name='detalle-libro'),
    path('autores/', AuthorListView.as_view(), name='lista-autores'),
    path('autores/<int:pk>', AuthorDetailView.as_view(), name='detalle-autor'),


]