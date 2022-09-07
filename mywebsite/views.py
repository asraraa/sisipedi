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
			
			# nip harus 18 digit
			if(len(nip) == 18):
				try:
					peserta = PesertaModel.objects.get(nip=nip)
					attended_diklat = peserta.diklat_id
					messages.error(request,attended_diklat)
					return redirect('index')
					
				except PesertaModel.DoesNotExist:
					peserta = None
					
					context = {
						'nip':nip
					}
					return redirect('diklat:register',nip=nip)
			
			else:
				messages.warning(request,'NIP harus 18 digit')
				return redirect('index')
	
	else:
		context = {
			'page_title':'Home',
			'title':'Pendaftaran Diklat',
			'background':'/img/bg-01.jpg',
			'peserta_form':peserta_form
		}

		return render(request,'index.html',context)