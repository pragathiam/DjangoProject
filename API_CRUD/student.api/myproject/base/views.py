from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from base.models import StudentsModel
from .serializers import StudentSerializer
import json
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser


@csrf_exempt

def students(request):
    if request.method == 'GET':

      # Create your views here.
      #complex data
      model_instance=StudentsModel.objects.all()

      #python data
      serialized_python_data=StudentSerializer(model_instance,many=True)

      py_data=serialized_python_data.data
      print(py_data)
      print(type(py_data))

      #json module
      # json_data=json.dumps(py_data)
      # print(json_data) #{"s_name": "dinesh", "s_rollno":11,"s_course": "comp"}
      # print(type(json_data)) #<class 'str'>
      #
      json_data=JSONRenderer().render(py_data)

      # return HttpResponse(json_data,connect_type-'application/json')
      # return JsonResponse(py_data,safe=False)

      return HttpResponse(json_data)

    if request.method == 'POST' :
      req_data=request.body
      print(req_data) # b'{"s_name": "vinay", "s_rollno": 79, "s_course": "IT"}'
      print(type(req_data)) # <class 'bytes'>


    if request.method == 'POST':

      #bytes json
      req_data=request.body
      #print(req_data) # b'("s_name": "vinay", "s_rollno" :70, "s_course": "IT")'
      # print(type(req_data)) # <class 'bytes'>  

      #streaming of json
      stream_data=io.BytesIO(req_data)
      #print(stream_data) # <_io.BytesIO object at 0x000002215c680c70>
      #print(type(stream_data)) # <class '_io.BytesIO'>

      # parsing (python_data)
      pydata=JSONParser().parse(stream_data)
      print(pydata)
      print(type(pydata))

      # deserialization
      deserialization_data=StudentSerializer(data=pydata)
      if deserialization_data.is_valid():
         deserialization_data.save()
         return JsonResponse({'msg','data submitted !!!'})
      
def student(request,pk):
  # old data
  try: 
    stu=StudentsModel.objects.get(id=pk)
    print(stu.s_name)
    
  except:
    return HttpResponse('something went wrong')

# new data
  if request.method =='PUT':
    req_data=request.body
    stream_data=io.BytesIO(req_data)
    pydata=JSONParser().parser(stream_data)
    print(pydata)
    print(type(pydata))

    de_sers=StudentSerializer(stu,pydata,partial=True)
    if de_sers.is_valid():
      de_sers.save()
      return JsonResponse({'msg':'data submitted for update!!!'})
    
    if request.method == 'DELETE':
      stu.delete()
      return JsonResponse({'msg:data deleted!!!'})




