import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


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
    



class ProductType(models.Model):
    main_category = models.CharField(max_length=100, verbose_name='category name')
    sub_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='sub category name')
    
    class Meta:
        verbose_name = 'Type of products'
        verbose_name_plural = 'Types of products'
    
    def __str__(self):
        return self.main_category
