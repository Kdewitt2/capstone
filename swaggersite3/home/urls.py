from django.urls import path, include
from django.apps import apps
from . import views
from .views import OrderCreateView, ProductDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('shop/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('blog/', views.blog, name='blog'),
    path('order/', OrderCreateView.as_view(), name='order'),
]