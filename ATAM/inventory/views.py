# from turtle import right
from django.shortcuts import render
from tracking.models import Asset,Tracker,Job
from .forms import AddAssetForm,AddTrackerForm,AddJobForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def index(request):
    asset = Asset.objects.all()
    tracker = Tracker.objects.all()
    job = Job.objects.all()
    context = {
        'asset':asset,
        'tracker':tracker,
        'job':job,
       
    }
    
    return render(request,'inventory/index.html',context)
@login_required()
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
@login_required()
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
@login_required()
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


def add_job(request):
    form = AddJobForm()
    if request.method == 'POST':
        form = AddJobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/inventory/')
    else:

        context = {
            'form':form
        }
        return render(request,'inventory/add_job.html',context)

def update_job(request,id):
    job = Job.objects.get(pk=id)
    if request.method == 'POST':
        form = AddJobForm(request.POST,instance=job)
        if form.is_valid():
            form.save()
            return redirect('/inventory/')
    else:
        form = AddJobForm(instance=job)

    return render(request, 'inventory/add_job.html', {'form': form})    

def delete_job(request,id):
    job_instance = Job.objects.filter(pk=id)
    job_instance.delete()
    return redirect('/inventory/')

