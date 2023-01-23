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
    
class FAQ_Category(models.Model):

    name = models.CharField(_('name'), max_length=100)
    sort_order = models.IntegerField(_('sort order'), default=0, help_text=_('The order you would like the faq questions to be displayed.'))

    class Meta:
        verbose_name = _("FAQ Category")
        verbose_name_plural = _("FAQ Categories")
        ordering = ['sort_order', 'name']

    def __str__(self):
        return self.name
   
class FAQ(models.Model):


    ACTIVE = 1
    INACTIVE = 0
    STATUS_CHOICES = (
        (ACTIVE,    _('Active')),
        (INACTIVE,  _('Inactive')),
        )
    
    
    question = models.TextField(_('question'))
    answer = models.TextField(_('answer'), blank=True)
    faq_category = models.ForeignKey(FAQ_Category, verbose_name=_('faq category'), related_name='questions')
    slug = models.SlugField(_('slug'), max_length=100)
    sort_order = models.IntegerField(_('sort order'), default=0, help_text=_('The order you would like the question to be displayed.'))
    status = models.IntegerField(_('status'),
        choices=STATUS_CHOICES, default=INACTIVE)
    
    created_on = models.DateTimeField(_('created on'), default=datetime.datetime.now)
    updated_on = models.DateTimeField(_('updated on'))
    created_by = models.ForeignKey(CustomUser, verbose_name=_('created by'),
        null=True)
    updated_by = models.ForeignKey(CustomUser, verbose_name=_('updated by'),
        null=True)    
    


    class Meta:
        verbose_name = _("Frequent asked question")
        verbose_name_plural = _("Frequently asked questions")
        ordering = ['sort_order', 'created_on']


    def __str__(self):
        return self.question



