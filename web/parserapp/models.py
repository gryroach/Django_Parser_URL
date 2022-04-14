from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField


class DomainModel(models.Model):

    url = models.URLField('URL', null=False, unique=True)
    domain = models.CharField('domain', max_length=255, blank=False)
    create_date = models.DateTimeField('Create date', null=False)
    update_date = models.DateTimeField('Update date', null=True, blank=True)
    country = models.CharField('Country', max_length=30, blank=True)
    isDead = models.BooleanField('isDead', default=False)
    A = ArrayField(models.CharField(max_length=20), blank=True, null=True)
    NS = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    CNAME = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    TXT = ArrayField(models.CharField(max_length=255), blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.url}"

    def save(self, *args, **kwargs):
        if not self.update_date:
            self.update_date = self.create_date
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains"
        ordering = ['domain']


class MxModel(models.Model):
    domain = models.ForeignKey(DomainModel, db_index=True, on_delete=models.CASCADE, related_name='MX')
    exchange = models.CharField('Exchange', max_length=255)
    priority = models.IntegerField('Priority', default=0)

    objects = models.Manager()

    def __str__(self):
        return f"{self.exchange} {self.priority}"
