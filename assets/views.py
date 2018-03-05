from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from django.contrib.auth.models import User

from .models import Assets, AssigningAsset
from .forms import AssetRequestForm

from django.db.models import Q

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

def requestAssetsApproval(request, user_id):
    criterion1 = Q(approver_id=user_id)
    criterion2 = Q(status__exact="Booked Asset")

    assigningAssets = AssigningAsset.objects.filter(criterion1 & criterion2)

    context = {
        'title': 'Need Your Approval',
        'assigningAssets': assigningAssets
    }

    return render(request, 'assets/request-assets-approval.html', context)

def detailAsset(request,id):
    asset = Assets.objects.get(id=id)

    form = AssetRequestForm()

    context = {
        'title': 'Detail List Asset',
        'asset': asset,
        'form': form
    }

    return render(request, 'assets/detail-asset.html', context)
    
@require_POST
def requestAssetsForm(request, asset_id):
    form = AssetRequestForm(request.POST)

    if form.is_valid():
        quantity = form.cleaned_data['quantity']
        approver = None

        if not request.user.profile.boss_id:
            status = 'Approved'
        else:
            status = 'Booked Asset'
            approver = User.objects.get(pk=request.user.profile.boss_id)

        assets = Assets.objects.get(pk=asset_id)

        assignAssets =  AssigningAsset(
            status=status, 
            requester=request.user, 
            approver = approver,
            assets = assets,
            quantity = quantity
        )

        assignAssets.save()

    return redirect('list')

def approvedRequestedAsset(request, assign_assets_id):
    assignAssets = AssigningAsset.objects.get(pk=assign_assets_id)

    assignAssets.status = 'Approved'

    assignAssets.save()

    return redirect('index')
