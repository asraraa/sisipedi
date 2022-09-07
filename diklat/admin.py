from django.contrib import admin

# Register your models here.
from .models import DiklatModel, GolonganModel, PesertaModel
# from import_export.admin import ExportActionMixin
from import_export.admin import ImportExportModelAdmin

from .resources import PesertaDetailsAdminResource

class PesertaDetailAdmin(ImportExportModelAdmin):
	list_display = ('nip','name','diklat_id','golongan','instansi','jabatan')
	resource_class = PesertaDetailsAdminResource

	fieldsets = [
		("NIP dan Nama", {"fields": ["nip","name"]}),
		("Detail Pekerjaan", {"fields":["instansi","golongan","jabatan"]}),
		("Inserted At", {"fields":["created_at"]})
	]
	readonly_fields = ("nip","created_at","golongan")


class DiklatAdmin(ImportExportModelAdmin):
	list_display = ('created_at','nama_diklat','golongan','jabatan','started_at','ended_at')

	fieldsets = [
		("ID dan Nama", {"fields": ["id","created_at","nama_diklat"]}),
		("Syarat golongan dan jabatan", {"fields":["golongan","jabatan"]}),
		("Waktu", {"fields":["started_at","ended_at"]})
	]
	readonly_fields = ("id","created_at")

admin.site.register(GolonganModel)
admin.site.register(DiklatModel, DiklatAdmin)
admin.site.register(PesertaModel,PesertaDetailAdmin)



# class PesertaAdmin(ExportActionMixin, admin.ModelAdmin):
# 	def formfield_for_foreignkey(self, db_field, request, **kwargs):
# 		if db_field.name == "diklat_id":
# 			kwargs["queryset"] = DiklatModel.objects.order_by('started_at')
# 			return super(PesertaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
        
# 	list_display = ('created_at','diklat_id','name','nip','golongan','asal_instansi')

# 	fieldsets = [
# 		("ID dan Nama", {"fields": ["nip","name"]}),
# 		("Golongan", {"fields":["golongan"]}),
# 		("Inserted At", {"fields":["created_at"]})
# 	]
# 	readonly_fields = ("nip","created_at")

