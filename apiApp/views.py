from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Jadwal
from .serializers import ImsyakSerializer


def error_404(request, exception):
    return render(request, '404.html')


@api_view(['GET', 'PUT', 'DELETE'])
def jadwal_detail(request, id):
    try:
        # Ambil data jadwal berdasarkan id yang diberikan
        jadwal_imsyak = Jadwal.objects.get(id=id)
    except Jadwal.DoesNotExist:
        # Jika data tidak ditemukan, kirimkan response error 404
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # kembalikan data jadwal dalam bentuk serialized
        serializer = ImsyakSerializer(jadwal_imsyak)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # update data jadwal yang ada dengan data yang diberikan dalam request
        serializer = ImsyakSerializer(jadwal_imsyak, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # hapus data jadwal yang ada
        jadwal_imsyak.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def jadwal_list(request):
    if request.method == 'GET':
        # ambil semua data jadwal dan kembalikan dalam bentuk serialized
        jadwal_imsyak = Jadwal.objects.all()
        serializer = ImsyakSerializer(jadwal_imsyak, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # buat data baru dengan data yang diberikan dalam request
        serializer = ImsyakSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Jika data yang diberikan tidak valid, kirimkan response error 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
