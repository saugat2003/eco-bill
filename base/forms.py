from django import forms
from django.core.exceptions import ValidationError
from .models import Organization, Customer, Invoice, InvoiceItem, Signature, Product

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'logo', 'address', 'contact_number']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    def clean(self):
        cleaned_data = super().clean()
        # Ensure at least one contact method is provided
        email = cleaned_data.get('email')
        phone = cleaned_data.get('phone')
        if not email and not phone:
            raise ValidationError("Please provide either an email or phone number")
        return cleaned_data

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['receipt_number', 'date', 'payment_method']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'payment_method': forms.Select()
        }

    def clean_receipt_number(self):
        receipt_number = self.cleaned_data.get('receipt_number')
        if Invoice.objects.filter(receipt_number=receipt_number).exists():
            raise ValidationError("This receipt number already exists")
        return receipt_number

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['product', 'quantity', 'unit_price']
        widgets = {
            'product': forms.TextInput(attrs={'class': 'form-control'}),  # Changed to TextInput widget
            'quantity': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'})
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise ValidationError("Quantity must be greater than zero")
        return quantity

    def clean_unit_price(self):
        unit_price = self.cleaned_data.get('unit_price')
        if unit_price <= 0:
            raise ValidationError("Unit price must be greater than zero")
        return unit_price







class SignatureForm(forms.ModelForm):
    class Meta:
        model = Signature
        fields = ['image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 5 * 1024 * 1024:  # 5MB limit
                raise ValidationError("Signature image must be under 5MB")
        return image