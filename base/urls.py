from django.urls import path
from . import views
from .views import invoice_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('create_receipt/', views.create_receipt, name='create_receipt'),
    path('create_organization', views.create_organization, name='create_organization'),
    path('signup/', views.signup, name='signup'),
    path('invoice/<int:invoice_id>/', invoice_view, name='invoice_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

