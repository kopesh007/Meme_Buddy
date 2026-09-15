from django.contrib import admin
from .models import Posts,cat

admin.site.register(cat)

# Register your models here.

class post_interface(admin.ModelAdmin):
    list_display = ('caption','date','cato')
    search_field = ('caption','date','Posts__cato')
    list_filter = ('cato',)

admin.site.register(Posts,post_interface)
