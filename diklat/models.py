from django.db import models
from .validators import validate_nip
from multiselectfield import MultiSelectField
from django.utils import timezone

# Create your models here.
class GolonganModel(models.Model):
	LIST_GOLONGAN = (
		('I/a','I/a'),
		('I/b','I/b'),
		('I/c','I/c'),
		('I/d','I/d'),
		('II/a','II/a'),
		('II/b','II/b'),
		('II/c','II/c'),
		('II/d','II/d'),
		('III/a','III/a'),
		('III/b','III/b'),
		('III/c','III/c'),
		('III/d','III/d'),
		('IV/a','IV/a'),
		('IV/b','IV/b'),
		('IV/c','IV/c'),
		('IV/d','IV/d'),
		('IV/e','IV/e'),
		)

	golongan = MultiSelectField(
		choI/ces = LIST_GOLONGAN,
		max_length=200
		)
	
	class Meta:
		verbose_name_plural = "Golongan"

	def __str__(self):
		return "{}.{}".format(self.I/d,self.golongan)

class DiklatModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	nama_diklat = models.CharField(max_length=255)
	
	LIST_GOLONGAN = (
		('I/a','I/a'),
		('I/b','I/b'),
		('I/c','I/c'),
		('I/d','I/d'),
		('II/a','II/a'),
		('II/b','II/b'),
		('II/c','II/c'),
		('II/d','II/d'),
		('III/a','III/a'),
		('III/b','III/b'),
		('III/c','III/c'),
		('III/d','III/d'),
		('IV/a','IV/a'),
		('IV/b','IV/b'),
		('IV/c','IV/c'),
		('IV/d','IV/d'),
		('IV/e','IV/e'),
		)

	golongan = MultiSelectField(
		choI/ces = LIST_GOLONGAN,
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
	diklat_I/d = models.ForeignKey(DiklatModel, on_delete=models.SET_NULL, blank=True, null=True)
	name = models.CharField(max_length=100) 
	#last_name = models.CharField(max_length=100)
	
	LIST_GOLONGAN = (
		('I/a','I/a'),
		('I/b','I/b'),
		('I/c','I/c'),
		('I/d','I/d'),
		('II/a','II/a'),
		('II/b','II/b'),
		('II/c','II/c'),
		('II/d','II/d'),
		('III/a','III/a'),
		('III/b','III/b'),
		('III/c','III/c'),
		('III/d','III/d'),
		('IV/a','IV/a'),
		('IV/b','IV/b'),
		('IV/c','IV/c'),
		('IV/d','IV/d'),
		('IV/e','IV/e'),
		)

	golongan = models.CharField(
		max_length=5,
		choI/ces = LIST_GOLONGAN,
		default = 'III/a',
		)

	asal_instansi = models.CharField(max_length=100) 

	class Meta:
		verbose_name_plural = "Peserta"
	
	def __str__(self):
		return "{}.{}".format(self.nip,self.name)

