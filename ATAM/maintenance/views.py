from django.shortcuts import render
from tracking.models import Location
from haversine import haversine
import time
from .models import *
from .forms import *
from django.shortcuts import redirect

# Create your views here.

def trackers_list():
    # get all values of column tracker fvrom maintenance table
    rows = list(Maintenance.objects.values_list("tracker"))

    # filter unique tracker ids
    trackerids = list(set([list(id)[0] for id in rows]))
    return trackerids

# get latest maintenace details of all trackers from maintenance table
def maintenance_detail():
    trackerids = trackers_list()
    print(trackerids)
    details = []

    asset_names = []
    
    for trackerid in trackerids:
        details.append(Maintenance.objects.filter(tracker=trackerid).order_by("-id")[0])
        asset_names.append(Location.objects.filter(tracker_id=trackerid)[0])
    return details, asset_names

def index(request):
    details = maintenance_detail()[0]
    asset_names = maintenance_detail()[1]
    return render(request, 'maintenance/index.html', {
        "locations": details,
        "names": asset_names

    })


# def total_distance(tracker_iD):
#     locations = Location.objects.filter(tracker_id=tracker_iD)
#     list_locations = list(locations)
#     # distances = []
#     asset_name = ''
#     # tracker_id = list_locations[0].tracker_id
#     msg = 'NO MAINTENACE SCHEDULE'
#     d = 0
#     for i in range(len(list_locations)-1):
#         point1 = (list_locations[i].lat, list_locations[i].lng)
#         point2 = (list_locations[i+1].lat, list_locations[i+1].lng)
#         # distance = haversine(point1, point2)
#         diff = 0.5422548807007272
#         distance = diff * haversine(point1, point2) + haversine(point1, point2)
#         # distances.append([distance, point1, point2, list_locations[i]])
#         asset_name = list_locations[i]
#         # asset_id = list_locations[i]
#         d += distance
#         if (d / 20) >= 1:
#             msg = 'CHANGE OIL'
#             break
#         else:
#             msg = 'NO MAINTENACE SCHEDULE'
#     output = [d, msg, asset_name]
#     return output


def driver(request, tracker_iD):
    try:
        maintenance = Maintenance.objects.filter(tracker=tracker_iD).order_by("-id")[0]
    except IndexError:
        maintenance = Maintenance.objects.create(tracker = tracker_iD, total_distance = 0)

    locations = Location.objects.filter(tracker_id=tracker_iD)
    list_locations = list(locations)
    # distances = []
    asset_name = list_locations[0]
    tracker_id = list_locations[0].tracker_id
    msg = 'NO MAINTENACE SCHEDULE'
    d = 0
    for i in range(len(list_locations)-1):
        point1 = (list_locations[i].lat, list_locations[i].lng)
        point2 = (list_locations[i+1].lat, list_locations[i+1].lng)
        # distance = haversine(point1, point2)
        diff = 0.5422548807007272
        distance = diff * haversine(point1, point2) + haversine(point1, point2)
        # distances.append([distance, point1, point2, list_locations[i]])
        # asset_name = list_locations[i]
        # asset_id = list_locations[i]
        d += distance
        if (d / maintenance.maintenance_limit) >= 1:
            msg = 'CHANGE OIL'
            # break
        else:
            msg = 'NO MAINTENACE SCHEDULE'
    # Add record only if total_distance changes
    # output = total_distance(tracker_iD)
    # d = output[0]
    # msg = output[1]
    # asset_name = output[2]
    try:
        prev_entry = Maintenance.objects.filter(tracker=tracker_iD).order_by("-id")[0]
        prev_entry_distance = float(prev_entry.total_distance)
        if round(d,4) != prev_entry_distance:
            # if round(d,4) >= prev_entry.maintenance_limit:
            #     new_entry = Maintenance.objects.create(tracker = tracker_iD, total_distance = d, description = msg, maintenance_status = "Pending")
            # else:
            #     new_entry = Maintenance.objects.create(tracker = tracker_iD, total_distance = d, description = msg)
            new_entry = Maintenance.objects.create(tracker = tracker_iD, total_distance = d, description = msg)
            if round(d,4) >= new_entry.maintenance_limit:
                new_entry.maintenance_status = "Pending"
                new_entry.save()
            else:
                new_entry.save()
    except:
        # if float(prev_entry.total_distance) >= prev_entry.maintenance_limit:
        #         new_entry = Maintenance.objects.create(tracker = tracker_iD, total_distance = d, description = msg, maintenance_status = "Pending")
        # else:
        new_entry = Maintenance.objects.create(tracker = tracker_iD, total_distance = d, description = msg)
        new_entry.save()
    print(msg)
    return render(request,'maintenance/driver.html',{
        "name": asset_name,
        "alert": msg,
        "distance": round(d,4),
        "trackerid": tracker_id
    })

# def trackerdetail(request, tracker_iD):
#     details = total_distance(tracker_iD)

#     distance = details[0]
#     asset_name = details[2]

#     return render(request,'maintenance/trackerdetail.html',{
#         "distance": distance,
#         "name": asset_name
#     })


# Update maintenance_limit


# def add_limit(request):
#     form = AddMaintenanceForm()
#     if request.method == 'POST':
#         form = AddMaintenanceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/maintenance/')
#     else:

#         context = {
#             'form':form
#         }
#         return render(request,'maintenance/update_limit.html',context)


def update_limit(request,tracker_iD):
    asset = Maintenance.objects.filter(tracker=tracker_iD).order_by("-id")[0]
    # asset_id = asset.id
    # asset = Maintenance.objects.get(id=asset_id)
    if request.method == 'POST':
        form = AddMaintenanceForm(request.POST, instance=asset)
        if float(asset.total_distance) >= asset.maintenance_limit:
            asset.maintenance_status = "Pending"
            asset.description = "CHANGE OIL"

        else:
            asset.maintenance_status = "Not Pending"
            asset.description = "NO MAINTENACE SCHEDULE"

        if form.is_valid():
            form.save()
            return redirect('/maintenance/')
        
    else:
        form = AddMaintenanceForm(instance=asset)

    return render(request, 'maintenance/update_limit.html', {'form': form}) 


def reset_status(request,tracker_iD):
    asset = Maintenance.objects.filter(tracker=tracker_iD).order_by("-id")[0]
    # make another entry in location table of same position to make total distance zero
    prev_loc = Location.objects.filter(tracker=tracker_iD).order_by("-id")[0]
    # if request.method == 'POST':
        # form = UpdateMaintenanceForm(request.POST, instance=asset)
    print(asset.maintenance_status)
    asset.maintenance_status = "Done"
    asset.description = "NO MAINTENACE SCHEDULE"
    asset.total_distance = 0
        # if form.is_valid():
            # form.save()
    asset.save()
    print(asset.maintenance_status)
    new_location = Location.objects.create(lat = float(prev_loc.lat), lng = float(prev_loc.lng), tracker_id = prev_loc.tracker_id)
    new_location.save()

    return redirect("/maintenance/")
    # else:

        # return redirect('/maintenance/')
