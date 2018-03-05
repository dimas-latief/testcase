from django.shortcuts import render
from .models import Assets

# Create your views here.
def index(request):
    context = {
        'title': 'Home'
    }

    return render(request, 'assets/index.html', context)

def list_assets(request):
    assets = Assets.objects.all()

    context = {
        'title': 'List Asset',
        'assets': assets
    }

    return render(request, 'assets/list-assets.html', context)


