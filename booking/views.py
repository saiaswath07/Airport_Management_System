from django.shortcuts import render
import cx_Oracle
import datetime
# Create your views here.
#def bookingaction(request):
   # return render(request,'booking.html')
    
#def searchflightaction(request):
    #return render(request,'searchflight.html')

    
fr=''
to=''
l=[]
arr_date=''
#dep_date=''
# Create your views here.
def bookingaction(request):
    if not request.session.get('islogged', False):
      return render(request,'login_page.html',{'bkmsg':'Please login to book the flight'})
    global fr,to,arr_date,dep_date,l
    if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
        if key=="flyfrom":
                fr=value
        if key=="flyto":
                to=value
        if key=="date1":
                arr_date=value
                #a=datetime.datetime.strptime(arr_date, '%Y-%m-%d').strftime('%d-%m-%y')
        #if key=="date2":
         #       dep_date=value
      #a="(your values are '{}','{}','{}','{}')".format(fr,to,arr_date,dep_date)
      #print(a)
      
      #c="SELECT * FROM Flight where from_='{}' and to_='{}'".format(fr,to)
      #select * FROM Flight WHERE to_char(cast(Arrival as date),'YYYY-DD-MM')='2022-01-10' and from_='Bangalore' and to_='Delhi' ;
      c="SELECT * FROM Flight where from_='{}' and to_='{}' and to_char(cast(Arrival as date),'YYYY-MM-DD')='{}'".format(fr,to,arr_date)
      cursor.execute(c)
      t=list(cursor.fetchall())
      
      #print("data",c)
      l=[]
      
      for i in range(len(t)):
        l.append(t[i])
      #print(l)
      return render(request,'dum.html',{'se':l})
    return render(request,'booking.html')   

def dumaction(request):
    return render(request,'dum.html',{'se':l})  

def webcheckinaction(request):
    return render(request,'webcheckin.html')  










def extractflytno(request):
    flightid=''
    if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      print("--------------------ext----------------------------------------------------------",d)
      #m.close()
      for key,value in d.items():
        if key=="flightid":
                flightid=value
        print("-***********************************************************************",flightid)       

      #c="SELECT * FROM Flight where from_='{}' and to_='{}' and to_char(cast(Arrival as date),'YYYY-MM-DD')='{}'".format(fr,to,arr_date)
      #cursor.execute(c)
      return render(request,'passenger.html',{'flightid':flightid})
    return render(request,'dum.html')    








