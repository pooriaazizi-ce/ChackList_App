from django.shortcuts import render,redirect
from .models import List
from django.contrib import messages

def home(request):
    if(request.method =='POST'):
        r= dict(request.POST)
        i = List.objects.create(item=r.__getitem__('item')[0],
                                start_date=r.__getitem__('start_date')[0],end_date=r.__getitem__('end_date')[0],
                                completed=False)
        i.save()
        messages.success(request, message='Item has been added to the list')

    all_items = List.objects.all()
    return render(request, 'Home.html', {'all_items': all_items})

def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, message='Item has been deleted')
    return redirect('Home')

def cross_off(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('Home')

def uncross(request,list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('Home')
