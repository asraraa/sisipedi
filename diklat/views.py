from django.shortcuts import render, redirect

# Create your views here.
from .forms import DiklatForm, PesertaForm
from .models import DiklatModel, PesertaModel
from datetime import datetime
from django.http import HttpResponse
from django.contrib import messages
import functools

def index(request):
	list_diklat = DiklatModel.objects.all()

	context = {
		'page_title':"List Diklat",
		'list_diklat':list_diklat
	}

	return render(request,'diklat/index.html',context)

def create(request):
	diklat_form = DiklatForm(request.POST or None)

	if request.method == 'POST':
		if diklat_form.is_valid():
			diklat_form.save()
			
			return redirect('diklat:index')

	context = {
		'page_title':'Add Diklat',
		'diklat_form':diklat_form
	}

	return render(request,'diklat/create.html',context)

def register(request,nip):
	register_form = PesertaForm(request.POST or None,initial={'nip':nip})
	
	if request.method == 'POST' and register_form.is_valid():
		# The diklat golongan requirements as list
		golongan_list = []
		diklat = register_form.cleaned_data.get('diklat_id')
		selected_diklat = DiklatModel.objects.filter(nama_diklat=diklat)
		gol_selected_diklat = selected_diklat[0].golongan
		
		for gol in gol_selected_diklat:
			golongan_list.append(gol)

		# Get selected golongan
		selected_golongan = register_form.cleaned_data.get('golongan')

		# Check whether the selected golongan meets the diklat golongan requirements
		if any(gol in selected_golongan for gol in gol_selected_diklat):
			register_form.save()
			messages.info(request, 'Pendaftaran Berhasil')
			return redirect('index')
		else:
			messages.info(request, 'Pendaftaran gagal. Golongan tidak memenuhi syarat')
			return redirect('index')

	else:
		context = {
			'page_title':'FORMULIR PENDAFTARAN PESERTA PELATIHAN',
			'register_form':register_form,
			'nip':nip,
			#'diklat_list':diklat_list
		}
		
		return render(request,'diklat/register.html',context)