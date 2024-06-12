from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from . import models
from . import serializers

@api_view(['POST'])
def signup(request):
    serializer = serializers.NeighborSerializer(data=request.data)
    if serializer.is_valid():
        neighbor = serializer.save()
        tokens = RefreshToken.for_user(neighbor)
        token_values = {
            'refresh' : str(tokens),
            'access' : str(tokens.access_token)
        }
        return Response(token_values, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def login(request):
    data = models.Neighbor.objects.all()
    serializer = serializers.NeighborSerializer(data, many=True)
    return Response({'neighbors' : serializer.data})