from django.db import models

from django.urls import reverse

import uuid

# Create your models here.
class Genre(models.Model):
    name =models.CharField(max_length =100,help_text= "Enter the genre like action,comedy,adventures")

    def __str__(self):
        return self.name

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
        display_genre.short_description = 'Genre'
    
class Book(models.Model):
    title=models.CharField(max_length=100)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null = True)
    summary = models.TextField(max_length=200,help_text="Enter the description")
    isbn = models.CharField('ISBN',max_length=13 ,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>' )
    genre = models.ManyToManyField(Genre,help_text = 'selct a genre for this book')

    class Meta:
        ordering =["title"]
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail',args=[str(self.id)] )



class Author(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length= 100 )
    date_of_birth = models.DateField(null =True,blank=True)
    date_of_death = models.DateField('died',blank = True,null =True)

    def __str__(self):
        return '{0},{1}'.format(self.first_name,self.last_name)

    def get_absolute_url(self):
        return reverse('author-detail',args=[str(self.id)])


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique key for a book instance")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]
        

    def __str__(self):
        
        return '{0}'.format(self.book)