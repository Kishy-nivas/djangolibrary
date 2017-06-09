from django.shortcuts import render
from .models import Author,Book,BookInstance,Genre
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
def index(request):
    author_count = Author.objects.all().count()
    book_count = Book.objects.all().count()
    bookinstance_count = BookInstance.objects.all().count()
    genre_count = Genre.objects.all().count()
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits']= num_visits + 1
    return render(request,'library/index.html',{'author_count' :author_count,
    'book_count':book_count,'bookinstance_count':bookinstance_count,'genre_count':genre_count,'num_visits' : num_visits })

class BookListView(generic.ListView):
    model = Book
    queryset =Book.objects.all()
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book 

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
class BookCreate(CreateView):
    model = Book
    fields= '__all__'
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')
class BookInstanceView(generic.ListView):
    model = BookInstance 
    fields = ['id','book','imprint']

def search(request):
    query = Book.objects.filter(Q(title__icontains = request.POST['searchbox']) |Q(summary__icontains = request.POST['searchbox']))
    return render (request, 'library/search.html',{'query': query})
