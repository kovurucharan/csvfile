from django.shortcuts import render

# Create your views here.
import csv, io
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from WebApp.models import Uploadfile
from django.core.files.storage import FileSystemStorage

def wish(request):
    return  HttpResponse("Welcome to csv files world")

# def file(request):
#     data=Uploadfile.objects.all()
#     prompt = {
#         'order': 'Order of the CSV should be Name,Email, Phone',
#         'profiles': data
#     }
#     if request.method=='GET':
#         return render(request,'MyApp/upload.html',{'prompt':prompt})
#
#     csv_file = request.FILES['file']
#     if not csv_file.name.endswith('.csv'):
#         messages.error(request, 'THIS IS NOT A CSV FILE')
#
#     data_set = csv_file.read().decode('UTF-8')
#     io_string = io.StringIO(data_set)
#     next(io_string)
#
#     for column in csv.reader(io_string, delimiter=',', quotechar="|"):
#         _, created = Uploadfile.objects.update_or_create(
#             Name=column[0],
#             Email=column[1],
#             Phone=column[2],
#         )
#     context = {}
#     return render(request,'MyApp/upload.html' ,context)

def thanks(request):
    return render(request,'MyApp/thanks.html')

def simple_upload(request):
    if request.method=='POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        print(myfile.name)
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        uploaded_file_url=fs.url(filename)
        return render(request,'MyApp/simpleup.html',{'uploaded_file_url':uploaded_file_url})
    return render(request,'MyApp/simpleup.html')



























