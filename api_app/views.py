from urllib import request
from urllib.request import Request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CartItemSerializer
from .models import CartItem
import urllib.request as request

class CartItemViews(APIView):
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Status": "Sucess", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"Status":"Failure","data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
