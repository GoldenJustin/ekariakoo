"""mwampambashop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from django.conf.urls.static import static
from mwampambashop import settings, views

urlpatterns = [
    path('admin/secure', admin.site.urls),
    path('', views.home, name='home'),
    path('about-us', views.about_us, name='about_us'),
    path('terms-and-conditions', views.terms_and_conditions, name='terms_and_conditions'),
    # path('', include(tf_urls)),
    path('authentication/', include('users.urls')),
    path('store/', include('product_store.urls')),
    path('cart/', include('product_cart.urls')),
    path('order/', include('product_order.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
