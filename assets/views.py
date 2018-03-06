from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from django.contrib.auth.models import User

from .models import Assets, AssigningAsset, Profile, Departments
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

def reportingEmployee(request):
    users = User.objects.exclude(pk=1)

    for item in users:
        item.totalSubordinates = Profile.objects.filter(boss_id=item.id).count()

    context = {
        'title': 'All Employee',
        'users': users
    }

    return render(request, 'assets/reporting-employee.html', context)

def reportingDepartment(request):
    departments = Departments.objects.all()

    for item in departments:
        item.totalEmployee = Profile.objects.filter(department_id=item.id).count()
        profiles = Profile.objects.filter(department_id=item.id).all()

        totalAssets = 0
        
        for profile in profiles:
            count = User.objects.get(pk=profile.user_id).requester_set.filter(status='Approved').count()
            totalAssets = totalAssets + count
            
        item.totalAsset = totalAssets

    context = {
        'title': 'All Department',
        'departments': departments
    }

    return render(request, 'assets/reporting-department.html', context)

def listEmployee(request):
    profiles = Profile.objects.exclude(pk=1)

    context = {
        'title': 'List Employee',
        'profiles': profiles
    }

    return render(request, 'assets/list-employee.html', context)

def employeeTree(request, user_id):
    target = Profile.objects.get(user_id=user_id)
    kepala = None
    
    if target.boss_id:
        kepala = Profile.objects.get(user_id=target.boss_id)

    tracker = set()
    condition = True
    tree = {}
    itungan = 0
    tree[itungan] = []
    tree[itungan].append(target.user.username)
    while condition:
        itungan += 1
        tree[itungan] = []
        if len(tracker) != 0:
            target = tracker.pop()

        perkumpulanAnak = cariAnak(target)
        if not perkumpulanAnak:
            condition = False
        else:
            for anak in perkumpulanAnak:
                tree[itungan].append(anak.user.username)
                tracker.add(anak)
        
    context = {
        'title': 'Employee Tree',
        'tree': tree,
        'kepala': kepala
    }

    return render(request, 'assets/tree-employee.html', context)

def cariAnak(target):
    anak = Profile.objects.filter(boss_id=target.user_id)
    return anak
