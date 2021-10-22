from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from product.models import Category, Product, Images, Comment

@staff_member_required
def reports(request, pk ):
    products = get_object_or_404(Product, pk=pk)
    context = {
        'product': products,
    }
    return render(request, 'admin/reports.html', context=context)
def get_reports(request, pk):
    products = get_object_or_404(Product, pk=pk)
    context = {
        'product':products,
    }
    return render(request, 'admin/product/get_reports.html', context=context)