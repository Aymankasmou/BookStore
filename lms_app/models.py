from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class book(models.Model):

    status_book = [
        ('availble','availble'),
        ('rental','rental'),
        ('sold','sold'),
    ]
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)    # author = المؤلف
    photo_book = models.ImageField(upload_to='photos', null=True, blank=True)
    photo_author = models.ImageField(upload_to='photos', null=True, blank=True)
    pages = models.IntegerField( null=True, blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)   # max_digits=5,decimal_places=2 => 12345,12
    retal_price_day = models.DecimalField(max_digits=5,decimal_places=2,null=True, blank=True)
    retal_period = models.IntegerField(null=True, blank=True)          # retal_period => مدة استاجار الكتاب
    total_rental= models.DecimalField(max_digits=5,decimal_places=2,null=True, blank=True)  #26
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices = status_book, null=True, blank=True)
    Category = models.ForeignKey(Category, on_delete= models.PROTECT, )
    def __str__(self):
        return self.title