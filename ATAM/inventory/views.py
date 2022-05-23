# from turtle import right
from django.shortcuts import render
from tracking.models import Asset,Tracker
from .forms import AddAssetForm,AddTrackerForm
from django.shortcuts import redirect
# Create your views here.

def index(request):
    asset = Asset.objects.all()
    tracker = Tracker.objects.all()
    context = {
        'asset':asset,
        'tracker':tracker,
       
    }
    
    return render(request,'inventory/index.html',context)

def add_asset(request):
    form = AddAssetForm()
    if request.method == 'POST':
        form = AddAssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inventory/')
    else:

        context = {
            'form':form
        }
        return render(request,'inventory/add_asset.html',context)

def update_asset(request,id):
    asset = Asset.objects.get(id=id)
    if request.method == 'POST':
        form = AddAssetForm(request.POST,instance=asset)
        if form.is_valid():
            form.save()
            return redirect('/inventory/')


    else:
        form = AddAssetForm(instance=asset)

    return render(request, 'inventory/add_asset.html', {'form': form})    

def delete_asset(request,id):
    print('-------------------')
    asset_instance = Asset.objects.filter(pk=id)
    print("deleted!",asset_instance)
    asset_instance.delete()
    return redirect('/inventory/')





def add_tracker(request):
    form = AddTrackerForm()
    if request.method == 'POST':
        form = AddTrackerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inventory/')
    else:

        context = {
            'form':form
        }
        return render(request,'inventory/add_tracker.html',context)

def update_tracker(request,id):
    tracker = Tracker.objects.get(pk=id)
    if request.method == 'POST':
        form = AddTrackerForm(request.POST,instance=tracker)
        if form.is_valid():
            form.save()
            return redirect('/inventory/')
    else:
        form = AddTrackerForm(instance=tracker)

    return render(request, 'inventory/add_tracker.html', {'form': form})    

def delete_tracker(request,id):
    tracker_instance = Tracker.objects.filter(pk=id)
    tracker_instance.delete()
    return redirect('/inventory/')