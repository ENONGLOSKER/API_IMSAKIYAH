from django.urls import path
from . import views

app_name='apiApp'

urlpatterns = [
    path('jadwal/<int:id>/',views.jadwal_detail), #dengan id (detail,edit dan hapus)
    path('jadwals/',views.jadwal_list), #tanpa id (menampilkan dan membuat)
]