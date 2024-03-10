from django.contrib import admin
from .models import Client, Address, Favorites, Cart, CartItem


class AddressAdmin(admin.TabularInline):
    model = Address
    extra = 1
    list_display = ('city', 'client')    


class ClientAdmin(admin.ModelAdmin):
    inlines = [AddressAdmin]
    list_display = ('user',)  


    
admin.site.register(Client, ClientAdmin)
admin.site.register(Favorites)
admin.site.register(Cart)
admin.site.register(CartItem)
