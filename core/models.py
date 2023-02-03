import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import CustomUser
class NewsCategory(models.Model):

    title = models.CharField(max_length=50, blank=False)

    class Meta:
        verbose_name_plural = 'News Categories'

    def __str__(self):
        return self.title

class News(models.Model):

   title = models.CharField(max_length=150)
   category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
   image = models.ImageField(upload_to='image/')
   detail = models.TextField()
   add_time = models.DateField(auto_now_add=True)
   slug = models.SlugField(max_length=100, null=True)


   class Meta:
        verbose_name_plural = 'News'
        ordering = ['-add_time']
   
   
   def __str__(self):
    return self.title 


class Country(models.Model):

    name = models.CharField(max_length=15, verbose_name='Name')
    enabled = models.BooleanField(default=True, verbose_name='Enabled')

    class Meta:
        verbose_name = 'Counrty'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name
    


class Currency(models.Model):

    name = models.CharField(max_length=4, verbose_name='currency name')
    sign = models.CharField(max_length=1, verbose_name='currency sign')
    rate = models.DecimalField(max_digits=5, decimal_places=4)


    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str_(self):
        return self.name
