from django.contrib import admin

# Register your models here.
from reservation.models import ReservationCart, RezervationProduct, Rezervation


class ReservationCartAdmin(admin.ModelAdmin):
    list_display = ['user','product','price','quantity','amount']
    list_filter = ['user']

class RezervationProductline(admin.TabularInline):
    model = RezervationProduct
    readonly_fields = ('user','product','price','quantity','amount')
    can_delete = False
    extra = 0

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','city','total','status']
    list_filter = ['status']
    readonly_fields = ('user','address','city','country','phone','first_name','ip','last_name','phone','city','total')
    can_delete = False
    inlines = [RezervationProductline]

class ReservationProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user']

admin.site.register(ReservationCart,ReservationCartAdmin)
admin.site.register(Rezervation,ReservationAdmin)
admin.site.register(RezervationProduct,ReservationProductAdmin)