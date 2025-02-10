# forms.py
from django import forms
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

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['receipt_number', 'date', 'payment_method']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['product', 'quantity', 'unit_price']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1}),
            'unit_price': forms.NumberInput(attrs={'step': '0.01'})
        }

InvoiceItemFormSet = forms.modelformset_factory(
    InvoiceItem,
    form=InvoiceItemForm,
    extra=1,
    can_delete=True
)

class SignatureForm(forms.ModelForm):
    class Meta:
        model = Signature
        fields = ['image']