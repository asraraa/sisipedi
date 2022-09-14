from django.shortcuts import render, redirect
from .forms import DiklatForm, PesertaForm
from .models import DiklatModel, PesertaModel
from datetime import datetime
from django.http import HttpResponse
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.forms import modelformset_factory
import functools

def index(request):
	list_diklat = DiklatModel.objects.all()

	context = {
		'page_title':'List Diklat',
		'title':'List Semua Diklat',
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
		'title':'Add Diklat',
		'diklat_form':diklat_form
	}

	return render(request,'diklat/create.html',context)

def register(request,nip):
	register_form = PesertaForm(request.POST or None,initial={'nip':nip})
	
	if request.method == 'POST' and register_form.is_valid():
		# The diklat golongan requirements as list
		# Also check the jabatan
		golongan_list = []
		jabatan_list = []

		diklat = register_form.cleaned_data.get('diklat_id')
		selected_diklat = DiklatModel.objects.filter(nama_diklat=diklat)

		gol_selected_diklat = selected_diklat[0].golongan
		jabatan_selected_diklat = selected_diklat[0].jabatan

		if (jabatan_selected_diklat is not None):
			split_jabatan = jabatan_selected_diklat.split(",")
			for jabatan in split_jabatan:
				jabatan_list.append(jabatan.lower())
	
		for gol in gol_selected_diklat:
			golongan_list.append(gol)

		# Get selected golongan and inputted jabatan
		selected_golongan = register_form.cleaned_data.get('golongan')

		inputted_jabatan = register_form.cleaned_data.get('jabatan')
		if (inputted_jabatan is not None):
			inputted_jabatan = inputted_jabatan.lower()
			
		# Check whether the selected golongan and inputted jabatan meets the diklat golongan and jabatan requirements
		if any(gol in selected_golongan for gol in gol_selected_diklat):
			if jabatan_selected_diklat is None:
				register_form.save()
				messages.success(request, 'Pendaftaran Diklat Anda Berhasil')
				return redirect('index')
			elif inputted_jabatan in jabatan_list :
				register_form.save()
				messages.success(request, 'Pendaftaran Diklat Anda Berhasil')
				return redirect('index')
			else:
				messages.info(request, 'Jabatan tidak memenuhi syarat')
				return redirect('index')

		else:
			messages.info(request, 'Golongan tidak memenuhi syarat')
			return redirect('index')

	context = {
		'page_title':'Registrasi',
		'title':'FORMULIR PENDAFTARAN DIKLAT FUNGSIONAL',
		'title2':'BADAN PENGEMBANGAN SUMBER DAYA MANUSIA',
		'title3':'PROVINSI SUMATERA BARAT',
		'register_form':register_form,
		'nip':nip,
	}
	
	return render(request,'diklat/register.html',context)
