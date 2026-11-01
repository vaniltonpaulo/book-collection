from django.contrib import admin

# Register your models here.

#section 2 -  step 2
from .models import Book

# Register Book so it shows up in the admin panel
admin.site.register(Book)