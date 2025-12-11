# Register your models here.
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "brand", "model", "price", "is_popular")
    list_filter = ("model", "is_popular")
    search_fields = ("brand", "title", "model")