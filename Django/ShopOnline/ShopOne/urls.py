"""ShopOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('img/', views.imageview, name='imageView'),
    path('home/', views.homeview, name='homeView'),
    path('search/', views.searchview, name='searchView'),
    path('prac/', views.pracview, name='pracView'),
    path('nav/', views.navview, name='navView'),
    path('contact/', views.contactview, name='contactView'),
    path('about/', views.aboutview, name='aboutView'),
    path('feedback/', views.feedbackview, name='feedbackView'),
    path('product/<int:pr_id>', views.productview, name='productView'),
    path('order', views.orderview, name='orderView'),
    path('cart/',views.cart_detailsview,name='cart_detailsView'),
    path('checkout/',views.checkoutview,name='checkoutView'),
    path('tracker/',views.trackerview,name='trackerView'),
    path('tracker_response/',views.tracker_responseview,name='tracker_responseView'),
    path('checkout_feedback/', views.checkout_feedbackview, name='checkout_feedbackView'),





] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
