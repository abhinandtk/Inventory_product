from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *



# Create your views here.
class CreateProductview(APIView):
    serializer_class=ProductSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data,"message":"Success","status":1},status=status.HTTP_201_CREATED)
        return Response({"message":serializer.errors,"status":0},status=status.HTTP_400_BAD_REQUEST)
    
class Getproduct(APIView):
    serializer_class=ProductSerializer
    def get(self,request):
        products=Products.objects.all()
        serializer=self.serializer_class(products,many=True)
        return Response({"data":serializer.data,"message":"success","status":1},status=status.HTTP_200_OK)

class Addstock(APIView):
    serializer_class=ProductSerializer
    def put(self,request):
        id=request.GET.get("id")
        stock=request.data.get("stock")
        try:
            product=Products.objects.get(id=id)
        except Products.DoesNotExist:
            return Response({"message": "Product not found", "status": 0}, status=status.HTTP_404_NOT_FOUND)
        serializer=self.serializer_class(product,data={"TotalStock":stock},partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"data":serializer.data,"message":"Updated successfully","status":1},status=status.HTTP_200_OK)
        return Response({"message": serializer.errors, "status": 0}, status=status.HTTP_400_BAD_REQUEST)
