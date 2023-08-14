from django.contrib import admin
from .models import Finch, Birdseed, Toy

# Register your models here.
admin.site.register(Finch)
admin.site.register(Birdseed)
admin.site.register(Toy)