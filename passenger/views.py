from django.shortcuts import render
import cx_Oracle
import string    
import random # define the random module  
from payment.views import paymentaction
# Create your views here.
#def passengeraction(request):
 #   return render(request,'passenger.html')
pfn=''
pln=''
gen=''
nan=''
flightno=''
phno=''
#ran = ''.join(random.choices(string.ascii_uppercase + string.digits,k =6)) 
#rand=str(ran)
#print("----------------------------------------------------",rand)

# Create your views here.
def passengeraction(request):
     global pfn,pln,gen,nan,flightno,phno
     if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
        if key=="pfname":
                pfn=value
        if key=="plname":
                pln=value
        if key=="pgender":
                gen=value
        if key=="pnan":
                nan=value
        if key=="flightid":
                flightno=value
        if key=="phno":
                phno=value        
      ran = ''.join(random.choices(string.ascii_uppercase + string.digits,k =6)) 
      request.session['pnr']=ran
        
        #if key=="rcpsw":
         #       cpwd=value

      #INSERT INTO Passenger VALUES('89Z7W0','sai','aswath','Male','Indian','yes','yes','B0731','s01','sec01');
          
      c="INSERT INTO Passenger VALUES('{}','{}','{}','{}','{}','no','no','{}','s01','sec01',null)".format(ran,pfn,pln,gen,nan,flightno)
      print("****************************************************************************",c)
      cursor.execute(c)
      m.commit() 

      ph="INSERT INTO  Passenger_ph VALUES('{}','{}')".format(ran,phno)
      cursor.execute(ph)
      m.commit() 
      #t=tuple(cursor.fetchall())
      #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",t)
      #m.commit() 
      return render(request,'payment.html')
     return render(request,'passenger.html') 









