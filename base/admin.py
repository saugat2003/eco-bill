from django.contrib import admin
from .models import Organization, Customer, PaymentMethod, Invoice, Product, InvoiceItem, Signature

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_number')
    search_fields = ('name', 'address')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
    search_fields = ('name', 'phone', 'email')

class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('method',)
    search_fields = ('method',)

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('receipt_number', 'customer', 'date', 'payment_method')
    search_fields = ('receipt_number', 'customer__name')
    list_filter = ('date',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'product', 'quantity', 'unit_price')
    search_fields = ('invoice__receipt_number', 'product__name')

class SignatureAdmin(admin.ModelAdmin):
    list_display = ('invoice',)
    search_fields = ('invoice__receipt_number',)

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(PaymentMethod, PaymentMethodAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
admin.site.register(Signature, SignatureAdmin)
