from django.db import models


class PackageStatus(models.Model):
    status_name = models.CharField(max_length=100)
    next_status = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    order = models.IntegerField()
    
    class Meta:
        verbose_name = 'Package Status'
        verbose_name_plural = 'Package Status'

    def __str__(self):
        return self.name