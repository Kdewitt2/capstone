from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect

from PIL import Image


class Product(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(default='defaultProd.jpg', upload_to='product_pics')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if(img.height > 170 or img.width > 200):
            output_size = (170,200)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return True

class HomePost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='home_pics')

    def __str__(self):
        return self.title

class Order(models.Model):
    guest = User.objects.filter(username="Guest").first()
    user = models.ForeignKey(User, default = guest, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(default=timezone.now())
    GrapefruitSoap = models.IntegerField(default=0)
    LemongrassSugarScrub = models.IntegerField(default=0)
    CharcoalClayFacialScrub = models.IntegerField(default=0)
    LavenderSoap = models.IntegerField(default=0)
    AloeVeraGoatMilkSoap = models.IntegerField(default=0)
    PeppermintSoap = models.IntegerField(default=0)
    EucalyptusSoap = models.IntegerField(default=0)
    RawSoap = models.IntegerField(default=0)
    CalendulaBurdockSalve = models.IntegerField(default=0)
    SootheMeSalve = models.IntegerField(default=0)
    LavenderLoofahSoap = models.IntegerField(default=0)
    LemonPoppySeedSoap = models.IntegerField(default=0)
        

    def __str__(self):
#        return "order by user at datetime {0}".format(date_ordered)
        return "order by {0} at datetime {1}".format(user, date_ordered)

    def get_absolute_url(self):
        return reverse('shop')
    

class ProductAmount(models.Model):
    order = models.ForeignKey(Order, db_index=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    amount = models.IntegerField(default=0)
    
