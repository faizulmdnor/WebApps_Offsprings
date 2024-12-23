from django.http import HttpResponse
from django.utils.safestring import mark_safe
import pyodbc


SERVER = 'FAIZULONXY\\SQLEXPRESS'
DATABASE = 'offsprings'

conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;')
cursor = conn.cursor()

def prestasi(request):
    
    return HttpResponse(prestasi)
