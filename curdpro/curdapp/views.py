from django.shortcuts import render,redirect
from .forms import ProductForm,UpdateForm,DeleteForm
from .models import ProductData
from django.http.response import HttpResponse
def home_view(request):
    return render(request,'home.html')
def product_insert_view(request):
    if request.method == 'POST':
        pform=ProductForm(request.POST)
        if pform.is_valid():
            p_id=request.POST.get('p_id','')
            p_name=request.POST.get('p_name','')
            p_cost=request.POST.get('p_cost','')
            p_color=request.POST.get('p_color','')
            p_class=request.POST.get('p_class','')
            c_name=request.POST.get('c_name','')
            c_mobile=request.POST.get('c_mobile','')
            c_email=request.POST.get('c_email','')
            pdata=ProductData(
                p_id=p_id,
                p_name=p_name,
                p_cost=p_cost,
                p_color=p_color,
                p_class=p_class,
                c_name=c_name,
                c_mobile=c_mobile,
                c_email=c_email
            )
            pdata.save()
            pform = ProductForm()
            return render(request, 'insert.html', {'pform': pform})
        else:
            return HttpResponse('invalid product id')

    else:
        pform=ProductForm()
        return render(request,'insert.html',{'pform':pform})


def product_update_view(request):
    if request.method=='POST':
        uform=UpdateForm(request.POST)
        if uform.is_valid():
            p_id=request.POST.get('p_id','')
            p_cost=request.POST.get('p_cost','')

            pdata1=ProductData.objects.filter(p_id=p_id)

            if not pdata1:
                return HttpResponse('invalid product')
            else:
                pdata1.update(p_cost=p_cost)
                uform=UpdateForm()
                return render(request,'update.html',{'uform': uform})
        else:
            return HttpResponse('invalid productid')

    else:
        uform=UpdateForm()
        return render(request,'update.html',{'uform':uform})


def product_retrieve_view(request):
    rdata=ProductData.objects.all()
    return render(request,'retrieve.html',{'rdata':rdata})


def product_delete_view(request):
    if request.method=='POST':
        dform=DeleteForm(request.POST)
        if dform.is_valid():
            p_id=request.POST.get('p_id','')
            rdata1=ProductData.objects.filter(p_id=p_id)
            if not rdata1:
                return HttpResponse('product id invalid')
            else:
                rdata1.delete()
                dform=DeleteForm()
                return render(request, 'delete.html', {'dform': dform})
        else:
            return HttpResponse('productid is invalid')
    else:
        dform=DeleteForm()
        return render(request,'delete.html',{'dform':dform})