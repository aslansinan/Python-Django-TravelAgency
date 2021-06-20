from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils.crypto import get_random_string
from home.models import UserProfile
from product.models import Category, Product
from reservation.models import ReservationCart, ReservationCartForm, ReservationForm, Rezervation, RezervationProduct


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

@login_required(login_url='/login')
def rezervationproduct(request):
    category = Category.objects.all()
    current_user = request.user
    schopcart = ReservationCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in schopcart:
            total += rs.product.price * rs.quantity

    if request.method == 'POST':  # if there is a post
        form = ReservationForm(request.POST)
        #return HttpResponse(request.POST.items())
        if form.is_valid():
            # Send Credit card to bank,  If the bank responds ok, continue, if not, show the error
            # ..............
            data = Rezervation()
            data.first_name = form.cleaned_data['first_name'] #get product quantity from form
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            reservationcode= get_random_string(5).upper() # random cod
            data.code =  reservationcode
            data.save() #

            schopcart = ReservationCart.objects.filter(user_id = current_user.id)
            for rs in schopcart:
                detail = RezervationProduct()
                detail.reservation_id     = data.id # Order Id
                detail.product_id   = rs.product_id
                detail.user_id      = current_user.id
                detail.quantity     = rs.quantity
                #****
                product = Product.objects.get(id=rs.product_id)
                product.amount -= rs.quantity
                product.save()
                #*****
                detail.price = rs.product.price
                detail.amount = rs.amount
                detail.save()
            ReservationCart.objects.filter(user_id=current_user.id).delete() # Clear & Delete shopcart
            request.session['cart_items']=0
            messages.Info(request, "Your Order has been completed. Thank you ")
            return render(request, 'Reservation_Completed.html',{'reservationcode':reservationcode,'category': category})
        else:
            messages.Warning(request, form.errors)
            return HttpResponseRedirect("/reservation/rezervationproduct")

    form= ReservationForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'schopcart': schopcart,
               'category': category,
               'total': total,
               'form': form,
               'profile': profile,
               }
    return render(request, 'Reservation_Form.html', context)