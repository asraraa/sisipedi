from django.contrib import admin

# Register your models here.
from .models import DiklatModel, GolonganModel, PesertaModel
from import_export.admin import ExportActionMixin

class DiklatAdmin(ExportActionMixin, admin.ModelAdmin):
	fieldsets = [
		("ID dan Nama", {"fields": ["id","created_at","nama_diklat"]}),
		("Golongan", {"fields":["golongan"]}),
		("Waktu", {"fields":["started_at","ended_at"]})
	]
	readonly_fields = ("id","created_at")

	#list_display = ('nama_diklat','golongan')

class PesertaAdmin(ExportActionMixin, admin.ModelAdmin):
	list_display = ('diklat_id','name','nip','golongan','asal_instansi')
	#form = PesertaForm

admin.site.register(GolonganModel)
admin.site.register(DiklatModel, DiklatAdmin)
admin.site.register(PesertaModel, PesertaAdmin)

