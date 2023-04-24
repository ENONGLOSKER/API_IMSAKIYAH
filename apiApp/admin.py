from django.contrib import admin
from . models import Jadwal

# Register your models here.
class jadwalModelAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated'] #untuk menmpilkan kolom yang tersembunyi
    list_display = ('tanggal','imsak','subuh','terbit','duha','zuhur','asar','magrib','isya','created','updated') #untuk menu pencarian berdasarkan kategori
    list_filter = ['tanggal'] #untuk membuat tampilkan tabel pada admin

admin.site.register(Jadwal,jadwalModelAdmin)