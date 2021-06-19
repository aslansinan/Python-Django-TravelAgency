from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from product.models import Category
from reservation.models import ReservationCart, ReservationCartForm


def index(request):
    return  HttpResponse("order App")

@login_required(login_url='/login')
def addtocart(request,id):
    url = request.META.get('HTTP_REFERER') # LAST URL
    if request.method == 'POST': #ürün detay kısmı
        form = ReservationCartForm(request.POST)
        if form.is_valid():
                current_user = request.user
                data = ReservationCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        request.session['cart_items']= ReservationCart.objects.filter(user_id=current_user.id).count()
        messages.Info(request,"ürün başarı ile sepete eklenmiştir. Teşekkür ederiz")
        return HttpResponseRedirect(url)

    else: #direkt sepet olayı
            current_user = request.user
            data = ReservationCart()
            data.user_id= current_user.id
            data.product_id = id
            data.quantity =1
            data.save()
            messages.Info(request, "ürün başarı ile sepete eklenmiştir. Teşekkür ederiz")
            return HttpResponseRedirect(url)
            request.session['cart_items'] = ReservationCart.objects.filter(user_id=current_user.id).count()
    messages.Warning(request, "ürün sepete eklemede hata oldu. Lütfen Kontrol ediniz")
    return HttpResponseRedirect(url)





@login_required(login_url='/login')
def reservationcart(request):
    category=Category.objects.all()
    current_user = request.user
    schopcart = ReservationCart.objects.filter(user_id=current_user.id)
    request.session['cart_items'] = ReservationCart.objects.filter(user_id=current_user.id).count()
    total = 0
    for rs in schopcart:
        total += rs.product.price * rs.quantity
    context = {
        'schopcart': schopcart,
        'category': category,
        'total': total,
    }
    return render(request,'Shopcart_products.html',context)

@login_required(login_url='/login')
def deleteformcart(request,id):
    ReservationCart.objects.filter(id=id).delete()
    current_user = request.user
    request.session['cart_items'] = ReservationCart.objects.filter(user_id=current_user.id).count()
    messages.Info(request, "ürün sepetten silinmiştir")
    return  HttpResponseRedirect("/reservationcart")