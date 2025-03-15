from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('about-book/<id>/', about_book, name="about_book"),
    path('genre/', genre, name="genre"),
    path('genre_book/<int:genre_id>/', genre_books, name='genre_books'),
    path('library/', library, name="library"),
    path('add-to-library/<book_id>/', add_to_library, name='add_to_library'),
    path('remove-library/<book_id>/', remove_library, name='remove_library'),
    path('new_releases/', new_releases, name="new_releases"),
    path('download-pdf/<id>/', download_pdf, name='download_pdf')
]