from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password
# Create your views here.


############# Beboer

@api_view(['POST'])
def password_check(request):
    serializer = BeboerSerializer(data=request.data)
    if serializer.is_valid():
        x = Beboer.objects.get(brugernavn=serializer.data['brugernavn'])
        if check_password(serializer.data['password'], x.password):
            return JsonResponse({'valid': 'True'})
        else:
            return JsonResponse({'valid': 'False'})
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def beboer_liste(request):
    b = Beboer.objects.all()
    serializer = BeboerSerializer(b, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def beboer_create(request):
    serializer = BeboerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def beboer_view(request, pk):
    b = Beboer.objects.get(id=pk)
    serializer = BeboerSerializer(b, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def beboer_update(request, pk):
    b = Beboer.objects.get(id=pk)
    serializer = BeboerSerializer(instance=b, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def beboer_delete(request, pk):
    b = Beboer.objects.get(id=pk)
    b.delete()

    return Response('Beboer Deleted Successfully')
############# Beboer_Slut


############# Location
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def location_liste(request):
    l = Location.objects.all()
    serializer = LocationSerializer(l, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def location_create(request):
    serializer = LocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def location_view(request, pk):
    l = Location.objects.get(id=pk)
    serializer = LocationSerializer(l, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def location_update(request, pk):
    l = Location.objects.get(id=pk)
    serializer = LocationSerializer(instance=l, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def location_delete(request, pk):
    l = Location.objects.get(id=pk)
    l.delete()

    return Response('location Deleted Successfully')
############# Location_Slut


############# Regler
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def regler_liste(request):
    r = Regler.objects.all()
    serializer = ReglerSerializer(r, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def regler_create(request):
    serializer = ReglerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def regler_view(request, pk):
    r = Regler.objects.get(postNr=pk)
    serializer = ReglerSerializer(r, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def regler_update(request, pk):
    r = Regler.objects.get(id=pk)
    serializer = ReglerSerializer(instance=r, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def regler_delete(request, pk):
    r = Regler.objects.get(id=pk)
    r.delete()

    return Response('Regler Deleted Successfully')
############# Regler_Slut


############# Andmeldelse
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def andmeldelse_liste(request):
    a = Andmeldelse.objects.all()
    serializer = AndmeldelseSerializer(a, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def andmeldelse_create(request):
    serializer = AndmeldelseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def andmeldelse_view(request, pk):
    a = Andmeldelse.objects.get(postNr=pk)
    serializer = AndmeldelseSerializer(a, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def andmeldelse_update(request, pk):
    a = Andmeldelse.objects.get(id=pk)
    serializer = AndmeldelseSerializer(instance=a, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def andmeldelse_delete(request, pk):
    a = Andmeldelse.objects.get(id=pk)
    a.delete()

    return Response('Andmeldelse Deleted Successfully')
############# PostNummer_Slut