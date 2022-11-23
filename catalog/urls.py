# urls de nuestra aplicaciÃ³n catalogo
from django.urls import path

from .views import (index, acerca_de,
                    BookListView, BookDetailView,
                    AuthorListView, AuthorDetailView,
                    SearchResultsListView,
                    renovar_libro,
                    librosprestados,
                     SearchResultsListView, AuthorCreate, AuthorUpdate, AuthorDelete, BookCreate, BookUpdate, BookDelete,
                     #success
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
    

    path('autores/create', AuthorCreate.as_view(), name='author-create'),
    path('autores/<int:pk>/update/', AuthorUpdate.as_view(), name='author-update'),
    path('autores/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),
    
    path('libros/create', BookCreate.as_view(), name='book-create'),
    path('libros/<int:pk>/update/', BookUpdate.as_view(), name='book-update'),
    path('libros/<int:pk>/delete/', BookDelete.as_view(), name='book-delete'),
    #Mensajes de éxito al guardar y modificar.
    #path('success/', success.as_view(), name='success'),
]