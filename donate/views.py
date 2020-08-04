from django.shortcuts import render
from .models import youdonate,donatethe

# Create your views here.

def donate(request):
    return render(request,"donatemain.html")

def donateyou(request):
    return render(request,"donateyou.html")

def thedonate(request):
    return render(request,"donatethe.html")

def end1(request):
    if request.method=="POST":
        ydname=request.POST["ydname"]
        ydaddress=request.POST["ydaddress"]
        yddaddress=request.POST["yddaddress"]
        ydcontact=request.POST["ydcontact"]
        ydpeople=request.POST["ydpeople"]
        ydfood=request.POST["ydfood"]
        yd=youdonate(ydname=ydname,ydaddress=ydaddress,yddaddress=yddaddress,ydcontact=ydcontact,ydpeople=ydpeople,ydfood=ydfood)
        yd.save()
        yd1={'ydname':ydname,'ydaddress':ydaddress,'yddaddress':yddaddress,'ydcontact':ydcontact,'ydpeople':ydpeople,'ydfood':ydfood}
        return render(request,"end1.html",yd1)
    else:
        return render(request,"donateyou.html")

def end2(request):
    if request.method=="POST":
        tdname=request.POST["tdname"]
        tdaddress=request.POST["tdaddress"]
        tdcontact=request.POST["tdcontact"]
        tdpeople=request.POST["tdpeople"]
        tdorphanage=request.POST["tdorphanage"]
        td=donatethe(tdname=tdname,tdaddress=tdaddress,tdcontact=tdcontact,tdpeople=tdpeople,tdorphanage=tdorphanage)
        td.save()
        td1={'tdname':tdname,'tdaddress':tdaddress,'tdcontact':tdcontact,'tdpeople':tdpeople,'tdorphanage':tdorphanage}
        return render(request,"end2.html",td1)
    else:
        return render(request,"donatethe.html")