from django.db import models

# Create your models here.
class books(models.Model):
     title = models.CharField(max_length=100)
     author = models.ForeignKey('Author', 
     on_delete=models.SET_NULL,#si se borra el autor, el libro se queda sin autor
      null=True)# puede ser nuñlo, pero no puede ser duplicado
     summary = models.TextField(max_length=1000
     , help_text='Enter a brief description of the book'# Create your models here.
     ,blank=True #no es obligatorio
     )
     isbn = models.CharField(max_length=13
     , max_length=13
     , help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
     genre = models.ManyToManyField('Genre'
     , help_text='Select a genre for this book')
     language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
     def __str__(self):
         return self.title
     def get_absolute_url(self):
         return reverse('book-detail', args=[str(self.id)])
class autor(models.Model):
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     date_of_birth = models.DateField(null=True, blank=True)
     date_of_death = models.DateField('Died', null=True, blank=True)
     def get_absolute_url(self):
         return reverse('author-detail', args=[str(self.id)])
     def __str__(self):
         return '{0}, {1}'.format(self.last_name, self.first_name)
class Genre(models.Model):
        name = models.CharField(max_length=200
        , help_text='Enter a book genre (e.g. Science Fiction)')
        def __str__(self):
            return self.name
class Language(models.Model):
        name = models.CharField(max_length=200
        , help_text='Enter the book\'s natural language (e.g. English, French, Japanese etc.)')
        def __str__(self):
            return self.name