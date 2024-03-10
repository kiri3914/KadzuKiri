from django.contrib import admin
from .models import Client, Adress, Favorites, Cart, CartItem


class AdressAdmin(admin.TabularInline):
    model = Adress
    extra = 1
    list_display = ('city', 'client')    


class ClientAdmin(admin.ModelAdmin):
    inlines = [AdressAdmin]
    list_display = ('user',)  


    
admin.site.register(Client, ClientAdmin)
admin.site.register(Favorites)
admin.site.register(Cart)
admin.site.register(CartItem)
