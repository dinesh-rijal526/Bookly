from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, RegexValidator

# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
    
class Genre(models.Model):
    genre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.genre
    

class Book(models.Model):
    title = models.CharField(max_length=100)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    pages = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)] 
    )
    
    genres = models.ManyToManyField(Genre, related_name='book')

    isbn = models.CharField(
        max_length=13,  # ISBN-13 has 13 characters
        unique=True,  # Ensures no two books have the same ISBN
        validators=[
            RegexValidator(
                regex=r'^(\d{10}|\d{13})$',
                message="ISBN must be either 10 or 13 digits long.",
            )
        ],
        help_text="Enter a 10-digit or 13-digit ISBN (numbers only)."
    )

    publication_date = models.DateField(null=True, blank=True)

    language = models.CharField(default='english', max_length=50)


    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='book/images')

    pdf = models.FileField(upload_to='book/pdfs')

    def __str__(self):
        return self.title
    

class Library(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'book'],
                name='unique_user_book_Library'
            )
        ]