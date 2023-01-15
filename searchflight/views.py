from django.shortcuts import render
#from searchflight.models import flightsearch
# Create your views here.
'''def searchflightaction(request):
    search=flightsearch.objects.all()
    print("output",search)
    return render(request,'searchflight.html',{'ser':search})'''


from django.shortcuts import render
import cx_Oracle
def searchflightaction(request):
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      #m.close()
      c="SELECT * FROM Flight "
      cursor.execute(c)
      t=list(cursor.fetchall())
      print(t)
      print(c)
      l=[]
      
      for i in range(len(t)):
        l.append(t[i])
      return render(request,'searchflight.html',{'ser':l})