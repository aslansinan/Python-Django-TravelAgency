"""project1 URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from home import views
from product.admin_views import get_reports, reports
from reservation import views as reservationviews
urlpatterns = [
    path('', include('home.urls')),
    path('hakkimizda', views.hakkimizda, name='hakkimizda'),
    path('referanslar', views.referanslar, name='referanslar'),
    path('iletişim', views.iletişim, name='iletişim'),
    path('product/', include('product.urls')),
    path('user/', include('user.urls')),
    path('reservation/', include('reservation.urls')),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>/<slug:slug>/',views.category_products,name='category_products'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/',views.product_search,name='product_search'),
    path('search_places/', views.search_places, name='search_places'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('faq/', views.faq, name='faq'),
    path('signup/', views.signup_view, name='signup_view'),
    path('reservationcart/', reservationviews.reservationcart, name='reservationcart'),
    path('admin/product/get_reports/<int:pk>/',get_reports,name='custom_get_reports'),
    path('admin/reports/<int:pk>/',reports,name='custom_reports'),
]
if settings.DEBUG: #new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)