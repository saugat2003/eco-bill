from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import *
from django.contrib import messages
from .forms import CustomerForm, InvoiceForm, SignatureForm, OrganizationForm, InvoiceItemForm
import logging

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def signup(request):
    return render(request, 'base/signup.html')

# @login_required
def create_receipt(request):
    try:
        organization = Organization.objects.get(user=request.user)
    except Organization.DoesNotExist:
        messages.error(request, 'Please create an organization first.')
        return redirect('create_organization')

    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if not customer_form.is_valid():
            messages.error(request, customer_form.errors)
            print("customer_form is not valid")

        invoice_form = InvoiceForm(request.POST)
        if not invoice_form.is_valid():
            messages.error(request, invoice_form.errors)
            print("hsdfsk is not valid")

        signature_form = SignatureForm(request.POST, request.FILES)
        if not signature_form.is_valid():
            print("dfghjkls;akd;s is not valid")
            messages.error(request, signature_form.errors)


        if customer_form.is_valid() and invoice_form.is_valid() and signature_form.is_valid():
            print("the data is saved")
            # Save customer
            customer = customer_form.save(commit=False)
            customer.organization = organization
            customer.save()

            # Save invoice
            invoice = invoice_form.save(commit=False)
            invoice.organization = organization
            invoice.customer = customer
            invoice.save()

            # # Save invoice items
            # instances = invoice_item_formset.save(commit=False)
            # for instance in instances:
            #     instance.invoice = invoice
            #     instance.save()

            # Handle deleted invoice items
            # for obj in invoice_item_formset.deleted_objects:
            #     obj.delete()

            # Save signature (corrected indentation)
            if signature_form.cleaned_data.get('image'):
                signature = signature_form.save(commit=False)
                signature.invoice = invoice
                signature.save()
            else:
                print("No signature provided")  # Optional: Can log this

            # Success message (outside loop)
            messages.success(request, 'Receipt created successfully!')
            return redirect('receipt_success_page')  # Redirect to avoid form resubmission

        else:
            print("the data is not saved")
            messages.error(request, 'Please correct the errors below.')

    else:
        # Initialize forms for GET request or after form error
        customer_form = CustomerForm()
        invoice_form = InvoiceForm()
        signature_form = SignatureForm()

    # Render form with context
    context = {
        'customer_form': customer_form,
        'invoice_form': invoice_form,
        'signature_form': signature_form,
        'products': Product.objects.filter(organization=organization),
        'payment_methods': PaymentMethod.objects.all(),
        'organization': organization,
    }
    return render(request, 'base/create_receipt.html', context)
# @login_required
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

def success(request):
    return render(request, 'base/success.html')

def about(request):
    return render(request, 'base/about.html')

def features(request):
    return render(request, 'base/features.html')

def pricing(request):
    return render(request, 'base/pricing.html')