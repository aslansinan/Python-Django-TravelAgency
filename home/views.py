from django.core.checks import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from home.models import Setting, ContactForm, ContactFormMessage
from product.models import Product, Category


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata= Product.objects.all()[:4]
    category=Category.objects.all()
    context = {'setting': setting,
               'page':'home',
               'category':category,
               'sliderdata':sliderdata}
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