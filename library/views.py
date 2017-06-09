from django.shortcuts import render
from .models import Author,Book,BookInstance,Genre
from django.views import generic
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    author_count = Author.objects.all().count()
    book_count = Book.objects.all().count()
    bookinstance_count = BookInstance.objects.all().count()
    genre_count = Genre.objects.all().count()
    return render(request,'library/index.html',{'author_count' :author_count,
    'book_count':book_count,'bookinstance_count':bookinstance_count,'genre_count':genre_count })

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
