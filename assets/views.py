from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


from .models import Assets
from .forms import AssetRequestForm

# Create your views here.
def index(request):
    context = {
        'title': 'Home'
    }

    return render(request, 'assets/index.html', context)

def listAssets(request):
    assets = Assets.objects.all()

    context = {
        'title': 'List Asset',
        'assets': assets
    }

    return render(request, 'assets/list-assets.html', context)

def detailAsset(request,id):
    asset = Assets.objects.get(id=id)

    form = AssetRequestForm()

    context = {
        'title': 'DetailList Asset',
        'asset': asset,
        'form': form
    }

    return render(request, 'assets/detail-asset.html', context)
    
@require_POST
def requestAssetsForm(request, user_id, asset_id):
    print (user_id)
    print (asset_id)
    # form = AssetRequestForm(request.POST)

    # print(request)
    # print(request.POST['quantity'])

    return redirect('index')
