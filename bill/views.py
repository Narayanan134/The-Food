from django.shortcuts import render

# Create your views here.

def orderinfo(request):
    return render(request,"orderinfo.html")
def bill(request):
    return render(request,"bill.html")