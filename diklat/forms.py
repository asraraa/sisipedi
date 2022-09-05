from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import NumberInput
from .models import DiklatModel, PesertaModel
from datetime import datetime

class DiklatForm(forms.ModelForm):
	
	class Meta:
		model = DiklatModel
		fields = [
			'nama_diklat',
			'started_at',
			'ended_at',
			'golongan',
		]

		labels = {
			'nama_diklat':'Nama Pelatihan',
			'golongan':'Syarat Golongan',
			'started_at':'Tanggal Mulai',
			'ended_at':'Tanggal Berakhir',
		}

		widgets = {
			'nama_diklat': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'Isikan Nama Diklat',
				}),
			'golongan': forms.CheckboxSelectMultiple(
				attrs = {
					'class':'btn-group',
			}),
			'started_at': forms.DateInput(
				attrs= {
					'type': 'date',
					'class':'form-control',
			}),
			'ended_at': forms.DateInput(
				attrs= {
					'type': 'date',
					'class':'form-control',
			}),
			
		}


class DiklatModelChoiceField(forms.ModelChoiceField):
	def label_from_instance(self, obj):
		label = f"{obj.nama_diklat}"
		return label
		

class PesertaForm(forms.ModelForm):
	diklat_id = DiklatModelChoiceField(queryset = DiklatModel.objects.filter(started_at__range = [datetime.now().date(), "2100-12-31"]), initial=0, widget=forms.Select(attrs={'class':'form-control'}))
	print(diklat_id)

	class Meta:
		model = PesertaModel

		fields = [
			'name',
			'nip',
			'golongan',
			'asal_instansi',
			'diklat_id',
		]

		labels = {
			'name':'Nama Lengkap',
			'nip':'NIP',
			'golongan': 'Golongan',
			'asal_instansi':'Asal Instansi',
			'diklat_id':'Pilih Pelatihan',
		}

		widgets = {
			'name': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'Isikan Nama Lengkap',
				}),
			'nip': forms.NumberInput(
				attrs = {
					'class':'form-control',
					'readonly':'readonly',
					 #'value':{{nip}},
			}),
			'golongan': forms.Select(
				attrs = {
					'class':'form-select',
			}),
			'asal_instansi': forms.TextInput(
				attrs= {
					'class':'form-control',
					'placeholder':'Isikan Asal Instansi',
			}),
			'diklat_id': forms.Select(
				attrs = {
					'class':'form-select',
			}),
			
		}

class IsEligibleForm(forms.ModelForm):
	class Meta:
		model = PesertaModel

		fields = [
			'nip',
		]

		labels = {
			'nip':'Masukkan NIP Anda',
		}

		widgets = {
			'nip': forms.NumberInput(
				attrs = {
					'class':'form-control',
					'placeholder':'cth: 199103192022062001',
				}),
		}


#class DiklatForm(forms.Form):
	#nama_diklat = forms.CharField(max_length=255)
	#golongan = forms.CharField(max_length=5)
	#date_added = forms.DateTimeField()
	#date_updated = forms.DateTimeField()
