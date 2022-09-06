from django.shortcuts import render, redirect
from diklat.models import DiklatModel, PesertaModel
from diklat.forms import IsEligibleForm
from datetime import datetime
from django.http import HttpResponse
from django.contrib import messages

def index(request):
	#diklat_form = DiklatModel.objects.filter(started_at__range = [datetime.now().date(), "2100-12-31"])
	peserta_form = IsEligibleForm(request.POST or None)

	if request.method == 'POST':
		if peserta_form.is_valid():
			nip = peserta_form.cleaned_data.get('nip')
			
			try:
				get_nip = PesertaModel.objects.get(nip=nip)
			
				messages.error(request,'NIP sudah terdaftar')
				
				return redirect('index')
			
			except PesertaModel.DoesNotExist:
				peserta = None
				#print(nip)
				context = {
					'nip':nip
				}
				return redirect('diklat:register',nip=nip)
	
	else:
		context = {
			'page_title':'Pendaftaran Pelatihan',
			# 'banner':'/img/banner_home.png',
			'peserta_form':peserta_form
		}

		return render(request,'index.html',context)