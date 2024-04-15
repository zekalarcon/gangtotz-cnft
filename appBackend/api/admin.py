from django.contrib import admin
from .models import Nft

class NftAdmin(admin.ModelAdmin):
    list_display = ('name', 'minted')
    exclude = ['image', 'thumbnail', 'slug']

# Register your models here.

admin.site.register(Nft, NftAdmin)