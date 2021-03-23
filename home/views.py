from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    text="Merhaba Django"
    context = {'text': text}
    return render(request, 'index.html', context)