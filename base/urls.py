from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('create_receipt/', views.create_receipt, name='create_receipt'),
    path('create_organization', views.create_organization, name='create_organization'),
    path('signup/', views.signup, name='signup'),
    path('success/', views.success, name='success'),
    path('about/', views.about, name='about'),
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

