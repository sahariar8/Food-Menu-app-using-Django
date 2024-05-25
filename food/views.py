from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def home(request):
    items = Item.objects.all()
    return render(request,'food/index.html',{'items':items})

def item(request):
    return HttpResponse("<h1>This is an Item View</h1>")

def detail(request,item_id):
    item = Item.objects.get(pk = item_id)
    return render(request,'food/detail.html',{'item':item})
