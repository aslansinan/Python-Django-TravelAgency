from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from home.models import Setting


def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'index.html', context)