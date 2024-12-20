import pyodbc
from django.http import HttpResponse
from django.utils.safestring import mark_safe

SERVER = 'FAIZULONXY\\SQLEXPRESS'
DATABASE = 'offsprings'

conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;')
cursor = conn.cursor()

def persekolahan(request):
    cursor.execute("""
        SELECT * 
        FROM vw_Persekolahan
        ORDER BY tahun, [Nombor K/P];
    """)
    persekolahan = cursor.fetchall()

    html_content = "<h1>Maklumat Persekolahan anak-anak.</h1>"
    html_content += "<table border='1'><tr>" + "".join(f"<th>{col[0]}</th>" for col in cursor.description) + "</tr>"
    html_content += "".join("<tr>" + "".join(f"<td>{str(cell)}</td>" for cell in row) + "</tr>" for row in persekolahan)

    return HttpResponse(mark_safe(html_content))