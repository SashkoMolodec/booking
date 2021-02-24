from django.contrib import admin

# Register your models here.
from .models import Hotel
from .models import Tag

admin.site.register(Hotel)
admin.site.register(Tag)

