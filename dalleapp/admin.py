from django.contrib import admin
from .models import Configuration,  Text
# Register your models here.

admin.site.register(Text)
admin.site.register(Configuration)