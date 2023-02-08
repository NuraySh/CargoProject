import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models import CustomUser
from core.abstracts import SingletonModel

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
    faq_category = models.ForeignKey(FAQ_Category, on_delete=models.CASCADE, verbose_name=_('faq category'), related_name='questions')
    slug = models.SlugField(_('slug'), max_length=100)
    sort_order = models.IntegerField(_('sort order'), default=0, help_text=_('The order you would like the question to be displayed.'))
    status = models.IntegerField(_('status'),
        choices=STATUS_CHOICES, default=INACTIVE)
    created_on = models.DateTimeField(_('created on'), default=datetime.datetime.now)
    updated_on = models.DateTimeField(_('updated on'))
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('created by'), related_name='+')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('updated by'),  related_name='+')    

    class Meta:
        verbose_name = _("Frequent asked question")
        verbose_name_plural = _("Frequently asked questions")
        ordering = ['sort_order', 'created_on']

    def __str__(self):
        return self.question
   
class ContactUs(SingletonModel):
    email = models.EmailField()
    phone = models.CharField(max_length=20) 
    address = models.TextField()
    work_hours = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

class ProductType(models.Model):
    main_category = models.CharField(max_length=100, verbose_name='category name', null=True)
    sub_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='sub category name')
    
    class Meta:
        verbose_name = 'Type of products'
        verbose_name_plural = 'Types of products'
    
    def __str__(self):
        return self.main_category

class Currency(models.Model):
    name = models.CharField(max_length=4, verbose_name='currency name')
    sign = models.CharField(max_length=1, verbose_name='currency sign')
    rate = models.DecimalField(max_digits=5, decimal_places=4)

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.name


class ForeignWarehouse(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='foreign country warehouse')
    is_active = models.BooleanField(default=True)
    airwaybill_address = models.CharField(max_length=255, verbose_name='airwaybill address')
    address_header = models.CharField(max_length=100, verbose_name='address header')
    name_surname = models.ManyToManyField(CustomUser,verbose_name='name and surname' )
    address_1 = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=15)
    mobile = models.CharField(max_length=20)
    gov_id = models.CharField(max_length=255, null=True, default='99674408434')

    class Meta:
        verbose_name = 'Foreign Warehouse'
        verbose_name_plural = 'Foreign Warehouses'

    def __str__(self):
        return self.country
    
    def save(self, *args, **kwargs):
        self.name_surname = CustomUser.get_full_name()
        super(ForeignWarehouse, self).save(*args, **kwargs)