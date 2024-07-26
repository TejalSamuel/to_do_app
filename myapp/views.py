from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Item

from django.contrib.auth.decorators import login_required


def index(request):
    items = Item.objects.all()
    return render(request, 'myapp/index.html', {'items': items})

@login_required
def home(request):
    return render(request, 'myapp/home.html')