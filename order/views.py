from django.shortcuts import render
from .models import img1,img2,img3,lunchh,breakfastt,dinnerr
# Create your views here.
def order(request):
    return render(request,"order.html")
def breakfast(request):
    image1=img1.objects.all()
    return render(request,"breakfast.html",{'image1':image1})
def lunch(request):
    image2=img2.objects.all()
    args={'image2':image2}
    return render(request,"lunch.html",args)
def dinner(request):
    image3=img3.objects.all()
    return render(request,"dinner.html",{'image3':image3})
def orderinfo(request):
    return render(request,"orderinfo.html")
def orderinfob(request):
    if request.method=="POST":
        qtyi=int(request.POST['qtyi'])
        qtyd=int(request.POST['qtyd'])
        qtypon=int(request.POST['qtypon'])
        qtyth=int(request.POST['qtyth'])
        qtyup=int(request.POST['qtyup'])
        qtypoo=int(request.POST['qtypoo'])
        args1={'qtyi':qtyi,'qtyd':qtyd,'qtypon':qtypon,'qtyth':qtyth,'qtyup':qtyup,'qtypoo':qtypoo}
        bt=breakfastt(qtyi=qtyi,qtyd=qtyd,qtypon=qtypon,qtyth=qtyth,qtyup=qtyup,qtypoo=qtypoo)
        bt.save()
        print(args1)
        return render(request,"orderinfob.html",args1)
    else:
        return render(request,"breakfast.html")
def orderinfod(request):
    return render(request,"orderinfod.html")
def bill(request):
    if request.method=="POST":
        nameofc=request.POST['nameofc']
        address=request.POST['address']
        contact=int(request.POST['contact'])

        args={'nameofc':nameofc,'address':address,'contact':contact}
        return render(request,"bill.html",args)
    else:    
        return render(request,"orderinfo.html")
    
    if request.method=="POST":
        qtycurd=request.POST['qtycurd']
        qtydal=request.POST['qtydal']
        qtylem=request.POST['qtylem']
        qtytam=request.POST['qtytam']
        qtyvr=request.POST['qtyvr']
        lu=lunchh(qtycurd=qtycurd,qtydal=qtydal,qtylem=qtylem,qtytam=qtytam,qtyvr=qtyvr)
        lu.save()
        args2={'qtycurd':qtycurd,'qtydal':qtydal,'qtylem':qtylem,'qtytam':qtytam,'qtyvr':qtyvr}
        return render(request,"orderinfo.html",args2)
    else:
        return render(request,"lunch.html")

    if request.method=="POST":
        qtyi=int(request.POST['qtyi'])
        qtyd=int(request.POST['qtyd'])
        qtypon=int(request.POST['qtypon'])
        qtyth=int(request.POST['qtyth'])
        qtyup=int(request.POST['qtyup'])
        qtypoo=int(request.POST['qtypoo'])
        args1={'qtyi':qtyi,'qtyd':qtyd,'qtypon':qtypon,'qtyth':qtyth,'qtyup':qtyup,'qtypoo':qtypoo}
        bt=breakfastt(qtyi=qtyi,qtyd=qtyd,qtypon=qtypon,qtyth=qtyth,qtyup=qtyup,qtypoo=qtypoo)
        bt.save()
        print(args1)
        return render(request,"orderinfob.html",args1)
    else:
        return render(request,"breakfast.html")

    if request.method=="POST":
        qtyi=request.POST['qtyi']
        qtyd=request.POST['qtyd']
        qtypon=request.POST['qtypon']
        qtyth=request.POST['qtyth']
        qtyup=request.POST['qtyup']
        qtypoo=request.POST['qtypoo']
        dn=dinnerr(qtyi=qtyi,qtyd=qtyd,qtypon=qtypon,qtyth=qtyth,qtyup=qtyup,qtypoo=qtypoo)
        dn.save()
        args3={'qtyi':qtyi,'qtyd':qtyd,'qtypon':qtypon,'qtyth':qtyth,'qtyup':qtyup,'qtypoo':qtypoo}
        return render(request,"orderinfod.html",args3)
    else:
        return render(request,"dinner.html")