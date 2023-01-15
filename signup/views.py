from django.shortcuts import render
import cx_Oracle

fn=''
ln=''
em=''
pwd=''
cpwd=''

# Create your views here.
def signaction(request):
     global fn,ln,em,pwd,cpwd
     if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
        if key=="rfname":
                fn=value
        if key=="rlname":
                ln=value
        if key=="remail":
                em=value
        if key=="rpsw":
                pwd=value
        if key=="rcpsw":
                cpwd=value
      c="INSERT INTO usr VALUES('{}','{}','{}','{}','{}')".format(fn,ln,em,pwd,cpwd)
      cursor.execute(c)
      m.commit() 
     return render(request,'signup_page.html',{'openregister':True}) 