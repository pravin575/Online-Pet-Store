"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/',include('shop.urls')),
    path('dogdry/',include('dogdry.urls')),
    path('dogwet/',include('dogwet.urls')),
    path('dogpuppy/',include('dogpuppy.urls')),
    path('doggrain/',include('doggrain.urls')),
    path('dogbake/',include('dogbake.urls')),
    path('dogveg/',include('dogveg.urls')),
    path('dogpremium/',include('dogpremium.urls')),
    path('catdry/',include('catdry.urls')),
    path('catwet/',include('catwet.urls')),
    path('kitten/',include('kitten.urls')),
    path('',include('user.urls')),
    path('cart/',include('cart.urls')),
    path('order/',include('checkout.urls')),
    path('reviews/', include('reviews.urls')),
    path('complaints/', include('complaints.urls')),
    path("returns/", include("returns.urls")),
    path('tracking/', include('tracking.urls')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
  