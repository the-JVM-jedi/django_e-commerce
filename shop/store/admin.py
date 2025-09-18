from django.contrib import admin
from .models import Category, Product, Order, OrderItem, Cart, CartItem

# Register your models here.

#Inline order items inside of Order
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0 #no empty rows by default

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('-created_at',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at', 'get_total_cost')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'id')
    inlines = [OrderItemInline]

    def get_total_cost(self, obj):
        return obj.get_total_cost()
    get_total_cost.short_description = "Total Cost"


@admin.register(OrderItem)
class OrderItem(admin.ModelAdmin):
    list_display = ('order', 'quantity', 'price', 'get_total_price')

    def get_total_price(self, obj):
        return obj.get_total_price()
    get_total_price.short_description = "Subtotal"

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", "get_total")
    def get_total(self, obj):
        return obj.get_total()
    get_total.short_description = "Cart Total"

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity", "get_total_price")
    def get_total_price(self, obj):
        return obj.get_total_price()
    get_total_price.short_description = "Subtotal"

