from django.core.checks import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from home.forms import SearchForm
from home.models import Setting, ContactForm, ContactFormMessage
from product.models import Product, Category, Images, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata= Product.objects.all()[:4]
    category=Category.objects.all()
    dayproducts=Product.objects.all()[:3]
    lastproducts=Product.objects.all().order_by('-id')[:3]
    randomproducts=Product.objects.all().order_by('?')[:3]
    context = {'setting': setting,
               'page':'home',
               'category':category,
               'sliderdata':sliderdata,
               'dayproducts': dayproducts,
               'lastproducts': lastproducts,
               'randomproducts': randomproducts,
               }
    return render(request, 'index.html', context)
def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'hakkimizda'}
    return render(request, 'hakkimizda.html', context)
def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'referanslar'}
    return render(request, 'referanslarimiz.html', context)
def iletişim(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data= ContactFormMessage()
            data.name =form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.Info(request,'Mesajınız Başarı İle Gönderilmiştir: Teşekkür Ederiz')
            return  HttpResponseRedirect ('/iletişim')
    setting = Setting.objects.get(pk=1)
    form = ContactForm()
    context = {'setting': setting, 'form':form}
    return render(request, 'iletişim.html', context)

def category_products(request,id,slug):
    category = Category.objects.all()
    categorydata =  Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = { 'products':products,
                'category':category,
                'categorydata':categorydata,
                }
    return render(request,'products.html',context)
def product_detail(request,id,slug):
    category = Category.objects.all()
    images = Images.objects.filter(product_id=id)
    comments =Comment.objects.filter(product_id=id,status='True')
    product = Product.objects.get(pk=id)
    context = {
               'category': category,
                'product': product,
                'images': images,
                'comments': comments
               }
    return render(request,'product_detail.html',context)
def product_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category=Category.objects.all()
            query=  form.cleaned_data['query']
            products =Product.objects.filter(title__icontains=query)
            context ={
                'products':products,
                'category':category,
            }
            return render(request,'product_search.html',context)

    return HttpResponseRedirect('/')