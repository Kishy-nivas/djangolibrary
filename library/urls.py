from django.conf.urls import url
from .import views
urlpatterns =[
    url('^$',views.index, name ='index'),  # matching with an empty string 
    url('^books/$',views.BookListView.as_view(),name ='books'),
    url('^book/(?P<pk>\d+)/$',views.BookDetailView.as_view(),name='book-detail'),
    url('^authors/$',views.AuthorListView.as_view(),name = 'author'),
    url('^author/(?P<pk>\d+)/$',views.AuthorDetailView.as_view(),name= 'author-detail'),
    url('^author/create/$',views.AuthorCreate.as_view(),name ='author-create'),
    url('^author/delete/(?P<pk>\d+)/$',views.AuthorDelete.as_view(),name='author-delete'),
    url('^author/update/(?P<pk>\d+)/$',views.AuthorUpdate.as_view(),name='author-update')


]