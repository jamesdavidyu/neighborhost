from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from . import models
from . import serializers

@api_view(['POST'])
def signup(request):
    serializer = serializers.NeighborSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def login(request):
    data = models.Neighbor.objects.all()
    serializer = serializers.NeighborSerializer(data, many=True)
    return Response({'neighbors' : serializer.data})