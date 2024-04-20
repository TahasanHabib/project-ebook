from django.contrib import admin

from .models import Catagory, Item # .models and admin.py are in the same directory

admin.site.register(Catagory)
admin.site.register(Item)
