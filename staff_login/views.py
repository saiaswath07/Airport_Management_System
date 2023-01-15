from django.shortcuts import render

# Create your views here.

import cx_Oracle
em=''
pwd=''
# Create your views here.
def staffloginaction(request):
     global em,pwd
     if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
 
        if key=="semail":
                em=value
        if key=="spsw":
                pwd=value
    
      c="SELECT * FROM staff where email='{}' and passsword='{}'".format(em,pwd)
      cursor.execute(c)
      t=cursor.fetchone()
      print(t)
      if not t:
            return render(request,'login_page.html',{'sf':'Invalid credentials','stafflogin':True})
      request.session['name']=t[1]+" "+t[2]
      ph="SELECT * FROM staff_ph where staff_id='{}'".format(t[0])
      cursor.execute(ph)
      ph=tuple(cursor.fetchone())
      
      return render(request,"staff_welcome.html",{'sname':t[1]+" "+t[2],'c':t,'ph':ph[1]})

     return render(request,'staff_page.html')
     
flytno=''
flytname=''
from_=''
to_=''
Adatetime=''
Ddatetime=''
av_seats=''
price=''
staffno=''
def addflightaction(request):
     global flytno,flytname,from_,to_,Adatetime,Ddatetime,av_seats,price,staffno
     if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
 
        if key=="fno":
                flytno=value
        if key=="fname":
                flytname=value
        if key=="fr":
                from_=value
        if key=="to":
                to_=value
        if key=="adate":
                Adatetime=value.replace('T', ' ') 
        if key=="ddate":
                Ddatetime=value.replace('T', ' ') 
        if key=="avseats":
                av_seats=value
        if key=="price":
                price=value 
        if key=="sno":
                staffno=value 
      print(Adatetime)#'2022-01-10 10:00:00      
      print(Ddatetime)                   
      c="INSERT INTO  Flight VALUES('{}','{}','{}','{}', to_date('{}','yyyy-mm-dd hh24:mi:ss'),to_date('{}','yyyy-mm-dd hh24:mi:ss'),{},{},'{}','n')".format(flytno,flytname,from_,to_,Adatetime,Ddatetime,av_seats,price,staffno)
      print(c)
      cursor.execute(c)
      m.commit()
      return render(request,'newflight.html',{'sname':request.session ['name'],'fadd':'Flight details are added successfully'})
     return render(request,'newflight.html',{'sname':request.session ['name']})
    


def manageflightaction(request):
      flightno=''
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
  
      if request.method=="POST":
     
      #m.close()
       for key,value in d.items():
        if key=="flyno":
                flightno=value
        print("-***********************************************************************",flightno)       
       d="UPDATE Flight SET deleted='y' WHERE Flight_no='{}'".format(flightno)
      
       cursor.execute(d)
       m.commit()
       print('--------------mn-----------------------------------------',d)
      c="SELECT * FROM Flight WHERE deleted='n'"
      cursor.execute(c)
      t=list(cursor.fetchall())
      #print(t)
      #print(c)
      l=[]
      for i in range(len(t)):
        l.append(t[i])
      return render(request,'manageflights.html',{'sname':request.session ['name'],'ser':l})
      