from django.db import models
from django.urls import reverse

# Create your models here.
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='Unknown')
    user_rating = models.DecimalField(max_digits=4, decimal_places=1)
    price = models.DecimalField(max_digits=4, decimal_places=0)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    genre = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='images/', default= 'images/default.jpg')

    class Meta:
        verbose_name_plural = 'Books'
        ordering = ('-user_rating',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def _str_(self):
        return self.title
