from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Registered user
    name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to='organization_logos/')
    address = models.TextField()
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Customer(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='customers')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class PaymentMethod(models.Model):
    method = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.method

class Invoice(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='invoices')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    receipt_number = models.CharField(max_length=50, unique=True)
    date = models.DateField()
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Invoice {self.receipt_number} - {self.customer.name}"

class Product(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_price(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.product.name} - {self.quantity} x {self.unit_price}"

class Signature(models.Model):
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE, related_name='signature')
    image = models.ImageField(upload_to='signatures/')

    def __str__(self):
        return f"Signature for Invoice {self.invoice.receipt_number}"
