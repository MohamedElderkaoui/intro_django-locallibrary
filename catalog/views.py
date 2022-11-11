from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Book, BookInstance, Author
from django.views.generic import ListView, DetailView
# Create your views here.
def index_old(request):
    texto = '''<h1>LibrerÃ­a Local</h1>
    <p>Esta es la pÃ¡gina principal de la librerÃ­a local.</p>'''
    # texto = 'PÃ¡gina inicial de la librerÃ­a local'
    lista = '<h2>Mi from django.shortcuts import renderlista de Ãºltimos libros</h2><ul>'
    # Consulta a la base de datos: Ãºltimos 5 libros
    # for libro in Book.objects.all()[:5]:
    # 5 Ãºltimos
    for libro in Book.objects.all().order_by('-id')[:5]:
        lista += f'<li>{libro.title}</li>'
    lista += '</ul>'  # fuera del for

    return HttpResponse(texto + lista)

def acerca_de(request):
    texto = '''<h1>Acerca de</h1>
    <p>Esta es la pÃ¡gina de acerca de de la librerÃ­a local.</p>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/EZ5sIrfmSwc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    
    '''
    return HttpResponse(texto)

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    UltimosLibros = Book.objects.all().order_by('-id')[:5]

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={
            'num_books':num_books,
            'num_instances':num_instances,
            'num_instances_available':num_instances_available,
            'num_authors':num_authors,
            'num_visits':num_visits
            ,'UltimosLibros':UltimosLibros},
    )
## Listas GenÃ©ricas
class BookListView(ListView):
    '''Vista genÃ©rica para el listado de libros'''
    model = Book
    paginate_by = 20
    

class BookDetailView(DetailView):
    '''Vista genÃ©rica para el detalle de un libro'''
    model = Book 

class AuthorListView(ListView):
    '''Vista genÃ©rica para el listado de autores'''
    model = Author
    paginate_by = 20

class AuthorDetailView(DetailView):
    '''Vista genÃ©rica para el detalle de un autor'''
    model = Author
#busqeuda
from django.shortcuts import render
class SearchResultsView(ListView):
    model = Book

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        return object_list
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context