from django.contrib import admin
from .models import Order, products,Order

# Register your models here.
class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    change_category_to_default.short_description="Default Category"
    list_display=('title','price','discount_price','category','description')
    search_fields = ('title','price','discount_price','category','description')
    actions=('change_category_to_default',)
    fields=('title','price',)
    list_editable=('price','category')
admin.site.register(products,ProductAdmin)
admin.site.register(Order)