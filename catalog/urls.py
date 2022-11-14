# urls de nuestra aplicaciÃ³n catalogo
from django.urls import path

from .views import (index, acerca_de,
                    BookListView, BookDetailView,
                    AuthorListView, AuthorDetailView,
                    #SearchResultsListView,
                    renovar_libro,
                    librosprestados,
                     SearchResultsListView,
                    )

urlpatterns = [
    path('', index, name='index'),
    path('acercade/', acerca_de, name='acercade'),
    path('libros/', BookListView.as_view(), name='lista-libros'),
    path('libros/<int:pk>', BookDetailView.as_view(), name='detalle-libro'),
    path('autores/', AuthorListView.as_view(), name='lista-autores'),
    path('autores/<int:pk>', AuthorDetailView.as_view(), name='detalle-autor'),
    path('prestados/', librosprestados.as_view(), name='prestados'),
    path('book/<uuid:pk>/renew/', renovar_libro, name='renovar-libro'),
    path('search/', SearchResultsListView.as_view(), name='buscar'),

]