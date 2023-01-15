from django.shortcuts import render,redirect
import cx_Oracle
em=''
pwd=''
# Create your views here.
def loginaction(request):
     global em,pwd
     if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
 
        if key=="lemail":
                em=value
        if key=="lpsw":
                pwd=value
    
      c="SELECT * FROM usr where email='{}' and passsword='{}'".format(em,pwd)
      cursor.execute(c)
      t=tuple(cursor.fetchall())
      print(t)
      if t==():
            return render(request,'login_page.html',{'openlogin':True,'msg':'Invalid Credentials'})
      else:
            request.session['islogged']=True
            return render(request,"login_page.html",{'loggedin': request.session['islogged'],'name':t[0][0] +" "+ t[0][1]})

     return render(request,'login_page.html')
     

def aboutusaction(request):
      return render(request,'aboutus.html')


def logout(request):
      request.session['islogged']=False
      return redirect('/login')

def signup_login(request):
  return render(request,"login_page.html",{'openlogin':True})  