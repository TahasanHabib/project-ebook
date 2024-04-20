from django.db import models
from django.contrib.auth.models import User

class Catagory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Catagories'
    
    def __str__(self):
        return self.name # this will be the name of the catagory in the admin panel
    
class Item(models.Model):
    category = models.ForeignKey(Catagory, related_name='items', on_delete=models.CASCADE) # if category is deleted, all items below that catagory will be deleted
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='iteam_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by =models.ForeignKey(User, related_name='items', on_delete=models.CASCADE) # if user is deleted, all items will be deleted
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name # this will be the name of the item in the admin panel
