from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import *
from django.contrib import messages
from .forms import CustomerForm, InvoiceForm, SignatureForm, InvoiceItemFormSet, OrganizationForm


# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def signup(request):
    return render(request, 'base/signup.html')

@login_required
def create_receipt(request):
    try:
        organization = Organization.objects.get(user=request.user)
    except Organization.DoesNotExist:
        messages.error(request, 'Please create an organization first.')
        return redirect('create_organization')
    
    if request.method == 'POST':
        try:
            with transaction.atomic():
                customer_form = CustomerForm(request.POST)
                invoice_form = InvoiceForm(request.POST)
                signature_form = SignatureForm(request.POST, request.FILES)
                invoice_item_formset = InvoiceItemFormSet(request.POST)
                
                if all(form.is_valid() for form in [
                    customer_form, invoice_form, 
                    signature_form, invoice_item_formset
                ]):
                    # Save customer
                    customer = customer_form.save(commit=False)
                    customer.organization = organization
                    customer.save()
                    
                    # Save invoice
                    invoice = invoice_form.save(commit=False)
                    invoice.organization = organization
                    invoice.customer = customer
                    invoice.save()
                    
                    # Save invoice items
                    instances = invoice_item_formset.save(commit=False)
                    for instance in instances:
                        instance.invoice = invoice
                        instance.save()
                    
                    # Handle deleted forms
                    for obj in invoice_item_formset.deleted_objects:
                        obj.delete()
                    
                    # Save signature
                    if signature_form.cleaned_data.get('image'):
                        signature = signature_form.save(commit=False)
                        signature.invoice = invoice
                        signature.save()
                    
                    messages.success(request, 'Receipt created successfully!')
                    return redirect('receipt_detail', pk=invoice.pk)  # Redirect to detail view
                else:
                    messages.error(request, 'Please correct the errors below.')
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            # Log the error here
    
    # GET request handling
    context = {
        'customer_form': CustomerForm(),
        'invoice_form': InvoiceForm(),
        'invoice_item_formset': InvoiceItemFormSet(queryset=InvoiceItem.objects.none()),
        'signature_form': SignatureForm(),
        'products': Product.objects.filter(organization=organization),
        'payment_methods': PaymentMethod.objects.all(),

        'organization': organization,
    }
    return render(request, 'base/create_receipt.html', context)

# def generate_receipt_number():
#     # Add your receipt number generation logic here
#     # This is a simple example
#     last_invoice = Invoice.objects.order_by('-id').first()
#     if last_invoice:
#         last_number = int(last_invoice.receipt_number.split('-')[1])
#         new_number = last_number + 1
#     else:
#         new_number = 1
#     return f'REC-{new_number:06d}'


@login_required
def create_organization(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST, request.FILES)
        if form.is_valid():
            organization = form.save(commit=False)
            organization.user = request.user
            organization.save()
            messages.success(request, 'Organization created successfully!')
            return redirect('create_receipt')
    else:
        form = OrganizationForm()
    
    return render(request, 'base/create_organization.html', {'form': form})

from .models import Invoice, InvoiceItem, Organization, Customer

