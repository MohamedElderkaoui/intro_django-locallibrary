from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from catalog.models import Book, BookInstance, Author
from django.views.generic import ListView, DetailView
from datetime import datetime
from catalog.forms import RenewBookForm


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
#busqeudaclass SearchResultsListView(ListView):
    model = Book
    
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        # voy a guardar query para el contexto
        self.query = query
        return Book.objects.filter(title__icontains=query)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SearchResultsListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['busqueda'] = self.query
        context['anterior'] = self.request.META.get('HTTP_REFERER')
        return context

class librosprestados(ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 20
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class librosprestadosadmin(ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_admin.html'
    paginate_by = 20
    
    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')

# vista para renovar un libro 

def renovar_libro(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # inicializa la fecha de renovaciÃ³n dentro de 3 semanas
    proposed_renewal_date = datetime.date.today() + \
        datetime.timedelta(weeks=3)
    form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})
    # 
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()
        else:
            # If this is a GET (or any other method) create the default form.

            context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/renovacion_fecha.html', context)
# SearchResultsListView

class SearchResultsListView(ListView):
    model = Book
    
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        # voy a guardar query para el contexto
        if query:
            self.query = query
            return Book.objects.filter(title__icontains=query)
        else:
            return []  
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SearchResultsListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['busqueda'] = self.query
        context['anterior'] = self.request.META.get('HTTP_REFERER')
        return context





