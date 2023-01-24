from django.db import models
from django.utils.translation import gettext_lazy as _


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
    


class ProductSubType(models.Model):

    title = models.CharField(max_length=100, verbose_name=_('product sub type name'))
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Product Sub Type")
        verbose_name_plural = _("Product Sub Types")
        ordering = ['title']

    def __str__(self):
        return self.title
class ProductType(models.Model):
     
     title = models.CharField(max_length=100, verbose_name=_('product type name'))
     sub_type_title = models.ForeignKey(ProductSubType, on_delete= models.CASCADE)
     is_active = models.BooleanField(default=True)

     class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")
        ordering = ['title']

     def __str__(self):
        return self.title

