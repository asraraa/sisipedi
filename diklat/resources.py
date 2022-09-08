from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget


from .models import PesertaModel, DiklatModel

class PesertaDetailsAdminResource(resources.ModelResource):
    class Meta:
        model = PesertaModel
        fields = (
            'nip',
            'name',
            'golongan',
            'jabatan',
            'instansi',
        )

    diklat = fields.Field(column_name='nama pelatihan', attribute='diklat_id', widget=ForeignKeyWidget(DiklatModel, field='nama_diklat'))
    diklat_mulai = fields.Field(column_name='tanggal mulai pelatihan', attribute='diklat_id', widget=ForeignKeyWidget(DiklatModel, field='started_at'))
    diklat_berakhir = fields.Field(column_name='tanggal akhir pelatihan', attribute='diklat_id', widget=ForeignKeyWidget(DiklatModel, field='ended_at'))
