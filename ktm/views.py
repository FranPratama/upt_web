from django.shortcuts import render, redirect
from django.contrib import messages
from ktm.forms import *
from ktm.models import *

# Create your views here.
def idc(request):
    if request.POST:
        form = FormKTM(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil ditambahkan !!")
            form = FormKTM()
            title = "Pembuatan KTM"
            context = {
                'form':form,
                'title':title,
            }
            return render(request, 'ktm.html', context)
    else:
        form = FormKTM()
        title = "Pembuatan KTM"
        context = {
            'form':form,
            'title':title,
        }
    return render(request,'ktm.html',context)