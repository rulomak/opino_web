from django.contrib import admin

# Register your models here.
from .models import Post,Category,City, Country

# Register your models here.
admin.site.register(Post)

admin.site.register(Category)

admin.site.register(City)

admin.site.register(Country)

