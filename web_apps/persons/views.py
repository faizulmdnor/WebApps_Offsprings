
from django.http import HttpResponse
from django.utils.safestring import mark_safe
import pyodbc


SERVER = 'FAIZULONXY\\SQLEXPRESS'
DATABASE = 'offsprings'

conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;')
cursor = conn.cursor()

def persons(request):
    cursor.execute("SELECT * FROM vw_Person")
    persons = cursor.fetchall()

    html_content = "<h1>Maklumat anak-anak.</h1>"
    html_content += "<table border='1'><tr>" + "".join(f"<th>{col[0]}</th>" for col in cursor.description) + "</tr>"
    html_content += "".join("<tr>" + "".join(f"<td>{str(cell)}</td>" for cell in row) + "</tr>" for row in persons)
    html_content += "</table>"
    return HttpResponse(mark_safe(html_content))


