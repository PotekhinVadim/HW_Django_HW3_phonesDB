from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to='images')
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)



