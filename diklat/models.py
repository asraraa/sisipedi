from django.db import models
from .validators import validate_nip
from multiselectfield import MultiSelectField
from django.utils import timezone

# Create your models here.
class GolonganModel(models.Model):
	LIST_GOLONGAN = (
		('Ia','Ia'),
		('Ib','Ib'),
		('Ic','Ic'),
		('Id','Id'),
		('IIa','IIa'),
		('IIb','IIb'),
		('IIc','IIc'),
		('IId','IId'),
		('IIIa','IIIa'),
		('IIIb','IIIb'),
		('IIIc','IIIc'),
		('IIId','IIId'),
		('IVa','IVa'),
		('IVb','IVb'),
		('IVc','IVc'),
		('IVd','IVd'),
		('IVe','IVe'),
		)

	golongan = MultiSelectField(
		choices = LIST_GOLONGAN,
		max_length=200
		)
	
	class Meta:
		verbose_name_plural = "Golongan"

	def __str__(self):
		return "{}.{}".format(self.id,self.golongan)

class DiklatModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	nama_diklat = models.CharField(max_length=255)
	
	LIST_GOLONGAN = (
		('Ia','Ia'),
		('Ib','Ib'),
		('Ic','Ic'),
		('Id','Id'),
		('IIa','IIa'),
		('IIb','IIb'),
		('IIc','IIc'),
		('IId','IId'),
		('IIIa','IIIa'),
		('IIIb','IIIb'),
		('IIIc','IIIc'),
		('IIId','IIId'),
		('IVa','IVa'),
		('IVb','IVb'),
		('IVc','IVc'),
		('IVd','IVd'),
		('IVe','IVe'),
		)

	golongan = MultiSelectField(
		choices = LIST_GOLONGAN,
		max_length=200
		)
	
	#status = models.BooleanField(default=False)

	started_at = models.DateField(default=timezone.now)
	ended_at = models.DateField(default=timezone.now)

	class Meta:
		verbose_name_plural = "Diklat"

	def __str__(self):
		return "{}".format(self.nama_diklat)


class PesertaModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	nip = models.CharField(max_length=30)
	diklat_id = models.ForeignKey(DiklatModel, on_delete=models.SET_NULL, blank=True, null=True)
	name = models.CharField(max_length=100) 
	#last_name = models.CharField(max_length=100)
	
	LIST_GOLONGAN = (
		('Ia','Ia'),
		('Ib','Ib'),
		('Ic','Ic'),
		('Id','Id'),
		('IIa','IIa'),
		('IIb','IIb'),
		('IIc','IIc'),
		('IId','IId'),
		('IIIa','IIIa'),
		('IIIb','IIIb'),
		('IIIc','IIIc'),
		('IIId','IIId'),
		('IVa','IVa'),
		('IVb','IVb'),
		('IVc','IVc'),
		('IVd','IVd'),
		('IVe','IVe'),
		)

	golongan = models.CharField(
		max_length=5,
		choices = LIST_GOLONGAN,
		default = 'IIIa',
		)

	asal_instansi = models.CharField(max_length=100) 

	class Meta:
		verbose_name_plural = "Peserta"
	
	def __str__(self):
		return "{}.{}".format(self.nip,self.name)

