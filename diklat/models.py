from django.db import models
from .validators import validate_nip
from multiselectfield import MultiSelectField
from django.utils import timezone
from django.core.validators import MinLengthValidator

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
		choices = LIST_GOLONGAN,
		max_length=200
		)
	
	jabatan = models.CharField(max_length=100,null=True,blank=True,help_text="Boleh kosong. Jika syarat lebih dari 1, pisahkan dengan karakter koma tanpa tambahan spasi (,). Contoh: Guru,Kepala Sekolah")
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
	#nip = models.CharField('Volume Number', max_length=18, validators=[MinLengthValidator(18)])
	diklat_id = models.ForeignKey(DiklatModel, on_delete=models.SET_NULL, blank=True, null=True)
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
		choices = LIST_GOLONGAN,
		default = 'IIIa',
		)

	instansi = models.CharField(max_length=100)
	jabatan = models.CharField(max_length=30, null=True,blank=True) 

	class Meta:
		verbose_name_plural = "Peserta"
	
	def __str__(self):
		return "{}.{}".format(self.nip,self.name)