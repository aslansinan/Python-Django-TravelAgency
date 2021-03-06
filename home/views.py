import json

from django.contrib.auth import logout, authenticate, login
from django.core.checks import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactForm, ContactFormMessage, UserProfile, FAQ
from product.models import Product, Category, Images, Comment
from reservation.models import ReservationCart


def index(request):
    current_user = request.user
    setting = Setting.objects.get(pk=1)
    sliderdata= Product.objects.all()[:4]
    category=Category.objects.all()
    dayproducts=Product.objects.all()[:6]
    lastproducts=Product.objects.all().order_by('-id')[:6]
    randomproducts=Product.objects.all().order_by('?')[:6]
    request.session['cart_items'] = ReservationCart.objects.filter(user_id=current_user.id).count()

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
    category = Category.objects.all()
    context = {'setting': setting, 'category': category, 'page':'hakkimizda'}
    return render(request, 'hakkimizda.html', context)
def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,'category':category, 'page':'referanslar'}
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
    category = Category.objects.all()
    form = ContactForm()
    context = {'setting': setting,'category':category, 'form':form}
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
            catid = form.cleaned_data['catid']
            if catid == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(title__icontains=query,category__id=catid)
            context ={
                'products':products,
                'category':category,
            }
            return render(request,'product_search.html',context)

    return HttpResponseRedirect('/')
def search_places(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    places = Product.objects.filter(title__icontains=q)
    results = []
    for rs in places:
      place_json = {}
      place_json = rs.title
      results.append(place_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.Info(request, 'Login Hatası! Kulanıcı adı yada şifre Yanlış')
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    context = {
               'category': category,
               }
    return render(request, 'login.html', context)
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get['username']
            password = form.cleaned_data.get['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.save()
            return HttpResponseRedirect('/')


    form = SignUpForm()
    category = Category.objects.all()
    context = {
        'category': category,
        'form': form,
    }
    return render(request, 'signup.html', context)


def faq(request):
    category = Category.objects.all()
    faq = FAQ.objects.all().order_by("ordernumber")
    context = {
        'faq': faq,
        'category': category,
    }
    return render(request, 'faq.html', context)