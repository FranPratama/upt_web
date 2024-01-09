from django.shortcuts import render, redirect
from django.contrib import messages
from hotspot.forms import *
from hotspot.models import *

# Create your views here.
def idhot(request):
    if request.POST:
        form = FormHotspot(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Form terkirim !!")
            form = FormHotspot()
            title = "Pembuatan Hotspot"
            context = {
                'form':form,
                'title':title,
            }
            return render(request, 'hotspot.html', context)
    else:
        form = FormHotspot()
        title = "Pembuatan Hotspot"
        context = {
            'form':form,
            'title':title,
        }
    return render(request,'hotspot.html',context)