from django.contrib import admin
from .models import Organization, Customer, PaymentMethod, Invoice, Product, InvoiceItem, Signature

# Register your models here.
admin.site.register(Organization)
admin.site.register(Customer)
admin.site.register(PaymentMethod)
admin.site.register(Invoice)
admin.site.register(Product)
admin.site.register(InvoiceItem)
admin.site.register(Signature)