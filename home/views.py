from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import *

# Create your views here.

def home(request):
    queryset = Book.objects.all()
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(title__icontains = search) |
            Q(author__name__icontains = search) |
            Q(genres__genre__icontains = search) |
            Q(isbn__icontains = search)
            ).distinct()
    context = {'books': queryset}
    return render(request, 'home/index.html', context)

@login_required
def about_book(request, id):
    queryset = Book.objects.get(id = id)
    context = {'book':queryset}
    return render(request, 'home/about_book.html', context)

@login_required
def genre(request):
    genres = Genre.objects.all()
    context = {'genres':genres}
    return render(request, 'home/genre.html', context)

def genre_books(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    books = Book.objects.filter(genres=genre)
    if request.GET.get('search'):
        search = request.GET.get('search')
        books = books.filter(
            Q(title__icontains = search) |
            Q(author__name__icontains = search) |
            Q(genres__genre__icontains = search) |
            Q(isbn__icontains = search)
            ).distinct()
    return render(request, 'home/genre_books.html', {
        'genre': genre,
        'books': books
    })

@login_required
def add_to_library(request,book_id):
    book = get_object_or_404(Book, id = book_id)
    library_item, created = Library.objects.get_or_create(
        user = request.user,
        book = book
    )
    if not created:
        library_item.save()
    return redirect('library')

@login_required
def library(request):
    queryset = Library.objects.filter(user = request.user)
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(title__icontains = search) |
            Q(author__name__icontains = search) |
            Q(genres__genre__icontains = search) |
            Q(isbn__icontains = search)
            ).distinct()
    context  = {'library':queryset}
    return render(request, 'home/library.html', context)

@login_required
def remove_library(request,id):
    wishlist = Library.objects.get(id = id)
    wishlist.delete()
    return redirect('library')

@login_required
def new_releases(request):
    queryset = Book.objects.order_by('-publication_date')
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(title__icontains = search) |
            Q(author__name__icontains = search) |
            Q(genres__genre__icontains = search) |
            Q(isbn__icontains = search)
            ).distinct()
    context = {'books': queryset}
    return render(request, 'home/new_releases.html', context)

@login_required
def download_pdf(request,id):
    book = Book.objects.get(id = id)
    file_path = book.pdf.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True)