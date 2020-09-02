from django.shortcuts import render,HttpResponse,redirect
from django.db.models import Q

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from datetime import datetime,timedelta
from .forms import *
import random


def index(request):
    error=''
    if request.method=='POST':
        user=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=user,password=password)
        try:
            if user.is_staff:
                login(request,user)
                error='no'
            else:
                error='yes'
        except:
            error='yes'

    context={'error':error}
    return render(request,'login.html',context)

def Logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def searchh(request):
    data=request.GET.get('searchdata')
    try:
        vehicle=Vehicle.objects.filter(Q(parkingNumber=data))
        vehicleCount=Vehicle.objects.filter(Q(parkingNumber=data)).count()
    except:
        vehicle=''
        vehicleCount=0

    print(vehicleCount,vehicle)
    context={'vehicle':vehicle,'vc':vehicleCount,'data':data}
    return render(request,'searchh.html',context)

@login_required(login_url='login')
def dashboard(request):
    today=datetime.now().date()
    yesterday=today-timedelta(1)
    week=today-timedelta(7)

    total_vehicle=Vehicle.objects.all().count()
    todays_vehicle=Vehicle.objects.filter(pdate=today).count()
    yesterday_vehicles=Vehicle.objects.filter(pdate=yesterday).count()
    lastWeek_total_vehicle=Vehicle.objects.filter(pdate__gt=week,pdate__lt=today).count()


    context={'totalv':total_vehicle,'tv':todays_vehicle,'yv':yesterday_vehicles,'lwv':lastWeek_total_vehicle}

    return render(request,'dashboard.html',context)

@login_required(login_url='login')
def add_category(request):
    error=''
    if request.method=='POST':
        categoryname=request.POST['categoryname']
        try:
            Category.objects.create(categoryName=categoryname)
            error='no'
        except:
            error='yes'
    print(error)
    context={}
    return render(request,'add_category.html',context)

@login_required(login_url='login')
def manage_category(request):
    cat=Category.objects.all()
    context={'category':cat}
    return render(request,'manage_category.html',context)

@login_required(login_url='login')
def delete_category(request,pid):
    cat=Category.objects.get(id=pid)
    cat.delete()
    return redirect('manage_category')

@login_required(login_url='login')
def add_vehicle(request):
    error=''
    cat=Category.objects.all()

    if request.method=='POST':
        parkingNumber=str(random.randint(10000000,99999999))
        ct=request.POST['category']
        vehicleCompany = request.POST['vehiclecompany']
        regNumber = request.POST['regno']
        ownerName = request.POST['ownername']
        ownerContact = request.POST['ownercontact']
        parkingDate = request.POST['pdate']
        inTime = request.POST['intime']

        status="In"
        category=Category.objects.get(categoryName=ct)

        try:
            
            Vehicle.objects.create(parkingNumber=parkingNumber,category=category,vehicleComapny=vehicleCompany,
                                   regNo=regNumber,ownerName=ownerName,ownerContact=ownerContact,
                                   pdate=parkingDate,inTime=inTime,status=status)
            error='no'
        except:
            error='yes'

    context={'error':error,'category':cat}
    return render(request,'add_vehicle.html',context)

@login_required(login_url='login')
def manage_invehicle(request):
    vehicle=Vehicle.objects.filter(status='In')
    context={'vehicle':vehicle}
    return render(request,'manage_invehicle.html',context)

@login_required(login_url='login')
def view_invehicle(request,pid):
    error=''
    vehicle=Vehicle.objects.get(id=pid)
    if request.method=='POST':
        rm=request.POST['remark']
        pc=request.POST['parkingcharge']
        ot=request.POST['outtime']
        status='Out'
        try:
            vehicle.remark=rm
            vehicle.parkingCharge=pc
            vehicle.outTime=ot
            vehicle.status=status
            vehicle.save()
            error='no'
        except:
            error='yes'

    print(vehicle)
    context={'vehicle':vehicle,'error':error}
    return render(request,'view_invehicle.html',context)

@login_required(login_url='login')
def manage_outvehicle(request):
    vehicle=Vehicle.objects.filter(status='Out')

    context={'vehicle':vehicle}
    print(vehicle)
    return render(request,'manage_outvehicle.html',context)

@login_required(login_url='login')
def view_outvehicle(request,pid):
    vehicle=Vehicle.objects.get(id=pid)
    context={'vehicle':vehicle}
    return render(request,'view_outvehicle.html',context)

def print_status(request,pid):
    vehicle = Vehicle.objects.get(id=pid)
    context = {'vehicle': vehicle}
    return render(request, 'print.html', context)

@login_required(login_url='login')
def visitors_between_dates(request):
    if request.method=='POST':
        fd=request.POST['fromdate']
        td=request.POST['todate']
        vehicle=Vehicle.objects.filter(Q(pdate__gte=fd) & Q(pdate__lte=td))
        vehicle_count=Vehicle.objects.filter(Q(pdate__gte=fd) & Q(pdate__lte=td)).count()
        context={'vehicle':vehicle,'vehicle_count':vehicle_count,'fd':fd,'td':td}
        return render(request,'visitor_between_date_details.html',context)

    return render(request,'visitors_between_dates.html')

@login_required(login_url='login')
def visitor_between_date_details(request):
    context={}
    return render(request,'visitor_between_date_details.html',context)

@login_required(login_url='login')
def change_password(request):
    error=''
    if request.method=="POST":
        current=request.POST['currentpassword']
        new=request.POST['newpassword']
        confirm=request.POST['confirmpassword']

        if new==confirm:
            user=User.objects.get(username__exact=request.user.username)
            user.set_password(new)
            user.save()
            error='no'
    context={'error':error}
    return render(request,'change_password.html',context)