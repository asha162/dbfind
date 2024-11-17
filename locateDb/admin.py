from django.contrib import admin
from .models import Search1, Search2, Search3


@admin.register(Search1)
class Search1Admin(admin.ModelAdmin):
    list_display = ('id', 'item')  

@admin.register(Search2)
class Search2Admin(admin.ModelAdmin):
    list_display = ('id', 'item') 

@admin.register(Search3)
class Search3Admin(admin.ModelAdmin):
    list_display = ('id', 'item')  
