from django.shortcuts import render
import cx_Oracle
# Create your views here.
email=''
name=''
country=''
phno=''
def contactusaction(request):
     global email,name,country,phno
     if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
        if key=="conem":
                email=value
        if key=="conname":
                name=value
        if key=="concountry":
                country=value
        if key=="conphno":
                phno=value        
      c="INSERT INTO contactus VALUES('{}','{}','{}',{})".format( email,name,country,phno)
      print(c)
      
      cursor.execute(c)
      m.commit() 
     return render(request,'contactus.html')


def passqueries(request):
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      #m.close()
      c="SELECT * FROM contactus "
      cursor.execute(c)
      t=list(cursor.fetchall())
      print(t)
      print(c)
      #l=t
      
      #for i in range(len(t)):
       # l.append(t[i])

      return render(request,'pass_queries.html',{'qu':t,'sname':request.session ['name']})