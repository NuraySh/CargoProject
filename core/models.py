from django.db import models


class NewsCategory(models.Model):

    title = models.CharField(max_length=50, blank=False)

    class Meta:
        verbose_name_plural = 'News Categories'

    def __str__(self):
        return self.title

class News(models.Model):

   title = models.CharField(max_length=150, blank=False, null=False)
   category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
   image = models.ImageField(upload_to='image/')
   detail = models.TextField(blank=False)
   add_time = models.DateField(auto_now_add=True)

   class Meta:
        verbose_name_plural = 'News'
   
   
   def __str__(self):
    return self.title 

