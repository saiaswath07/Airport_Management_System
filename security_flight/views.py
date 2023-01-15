from django.shortcuts import render
import cx_Oracle
# Create your views here.
def securitystarusaction(request):
    sec_pnr=''
    
    if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
  
      for key,value in d.items():
        if key=="sepnr":
                sec_pnr=value
      print("fdddddddddddddddddddddd",sec_pnr)

      print("fgdhjmhhgfghjrhfhjfthgtrhhtydj")
      c="UPDATE Passenger set Security_Status='yes' WHERE PNR='{}'".format(sec_pnr)
      cursor.execute(c)
      m.commit()

      return render(request,'security.html',{'msg':"PNR NO: {} has completed security checkup".format(sec_pnr),'secname':request.session ['secname']})
      #t=list(cursor.fetchall())
      #print(t)
    
    return render(request,'security.html',{'msg':'','secname':request.session ['secname']})



secem=''
secpwd=''
# Create your views here.
def securityloginaction(request):
     global secem,secpwd
     if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
 
        if key=="secemail":
                secem=value
        if key=="secpsw":
                secpwd=value
    
      c="SELECT * FROM Security_Officer WHERE email='{}' and passsword='{}'".format(secem,secpwd)
      cursor.execute(c)
      t=cursor.fetchone()
      if not t:
            return render(request,'login_page.html',{'secf':'Invalid credentials','seclogin':True})
      request.session['secname']=t[1]+" "+t[2]
      ph="SELECT * FROM Security_Officer_ph WHERE sec_id='{}'".format(t[0])
      cursor.execute(ph)
      ph=tuple(cursor.fetchone())
      
      print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",t)
    
      return render(request,"security_welcome.html",{'sname':t[1]+" "+t[2],'c':t,'ph':ph[1]})

     return render(request,'login_page.html')   