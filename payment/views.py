from django.shortcuts import render
import cx_Oracle
import string    
import random # define the random module  
import time
# Create your views here.
#def paymentaction(request):
 #   return render(request,'payment.html')




cno=''
cname=''
exp=''
cvv=''


# Create your views here.
def paymentaction(request):
     global cno,cname,exp,cvv
     if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
        if key=="ccnum":
                cno=value
        if key=="cardname":
                cname=value
        if key=="cardexp":
                exp=value
        if key=="cardcvv":
                cvv=value
      a = ''.join(random.choices(string.digits,k =4)) 
      ran='ck'+a       
      
      c="INSERT INTO Webvisitor_card VALUES('{}','{}','{}','{}',TO_DATE('{}','YYYY-MM'))".format(ran,cno,cname,cvv,exp)

      cursor.execute(c)
      m.commit()
      time.sleep(5)
      return render(request,'card.html')
     return render(request,'payment.html') 


def successaction(request):
 return render(request,'card.html')





