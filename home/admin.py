from django.contrib import admin
from .models import NutType, Nut, Category
# Register your models here.
class NutAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price", "stock"]
    list_editable = ["price","stock"]
    search_fields = ["name"]
    list_per_page = 2
    
admin.site.register(NutType)
admin.site.register(Nut, NutAdmin)
admin.site.register(Category)
