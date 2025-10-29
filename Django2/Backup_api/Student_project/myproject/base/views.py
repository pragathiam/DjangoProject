from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def student(request):
    # Read
    if request.method == 'GET':
        serialized_py=StudentSerializer(StudentModel.objects.all(),many=True)
        return Response(serialized_py.data)
    # Create
    if request.method=='POST':
        req_data=request.data
        ser_data=StudentSerializer(data=req_data)
        if ser_data.is_valid():
            ser_data.save()
            return Response(status=status.HTTP_201_CREATED)
        

@api_view(['PUT','GET','DELETE'])
def student(request,pk):
    # old data
    try:
        stu=StudentModel.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)  

    if request.method == 'GET':
        serialized_py=StudentSerializer(stu)  
        return Response(serialized_py.data)
    
    # Update
    if request.method=='PUT':
        req_data=request.data
        ser_data=StudentSerializer(stu,data=req_data,partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(status=status.HTTP_201_CREATED)
        
        # Delete
        if request.method=='DELETE':
            stu.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

           
        
