from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Stall(models.Model):
    Gravel = "Gravel"
    Concrete = "Concrete"
    name = models.CharField(max_length=200)
    description = models.TextField()
    floor_type = models.CharField(max_length=256,choices=[(Gravel, 'Gravel'),(Concrete,'Concrete')])
    door_height = models.DecimalField(max_digits=5,decimal_places=3)
    width = models.DecimalField(max_digits=5,decimal_places=3)
    length = models.DecimalField(max_digits=5,decimal_places=3)
    number_of_units = models.PositiveIntegerField()
    quarterly_rate = models.DecimalField(max_digits=6,decimal_places=2)
    pic = models.ImageField(upload_to='stall_pics/',blank=True,default="images/default_unit.jpg")
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stall_list')

    def save(self):
        self.slug = slugify(self.name)
        return super().save()
