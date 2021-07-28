from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'genres'

    # def get_absolute_url(self):
    #    return reverse()
    
    def _str_(self):
        return self.name
    
class Book(models.Model):
    genre = models.ForeignKey(Genre, related_name='product', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='Unknown')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    user_rating = models.DecimalField(max_digits=3, decimal_places=2)
    year = models.DecimalField(max_digits=4, decimal_places= 2)

    class Meta:
        verbose_name_plural = 'Books'
        ordering = ('user_rating',)

    def _str_(self):
        return self.title
