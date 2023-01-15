from django.shortcuts import render
import cx_Oracle
# Create your views here.

wpnr=''
wfn=''
wln=''
l=''

def webcheckinaction(request):
    if not request.session.get('islogged', False):
      return render(request,'login_page.html',{'bkmsg':'Please Login to webcheck in'})
    global wpnr,wfn,wln,l
    if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
        if key=="pnrno":
                wpnr=value
        if key=="pnrfn":
                wfn=value
        if key=="pnrln":
                wln=value
      c="SELECT * FROM Passenger WHERE PNR='{}' and Fname='{}' and Lname='{}'".format(wpnr,wfn,wln)
      cursor.execute(c)
    
      #m.commit()
      print(c)
      #t=list(cursor.fetchall())
      if not c:
        return render(request,'web_check.html', {'webmsg': 'Invalid credentials'})
      #print(t)
      
    return render(request,'web_check.html')

def checkindetailsaction(request):
    pnr=''
    seats = ['1A', '1C', '1D', '1F']
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(2, 15):
     seats.extend(['{}{}'.format(i, l) for l in letters])
    if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
        if key=="pnrno":
                pnr=value
        if key=="pnrfn":
                wfn=value
        if key=="pnrln":
                wln=value
      c="SELECT * FROM Passenger WHERE PNR='{}' and Fname='{}' and Lname='{}'".format(pnr,wfn,wln)
      cursor.execute(c)
    
      #m.commit()
      t=list(cursor.fetchall())
      print(t)
      if not t:
        return render(request,'web_check.html', {'webmsg': 'Invalid credentials'})
      q="SELECT seat_no FROM Passenger WHERE PNR='{}'".format(pnr)
      cursor.execute(q)
      a=cursor.fetchone()
      print("-----------------------------------",a)
      if a[0]:
        return render(request,'web_check.html',{'webmsg':'Your web checkin has already processed'})
      c="Select PNR,concat(Fname, concat(' ', Lname)) AS name,Flight.Flight_no,from_,to_,Arrival from Passenger, Flight where Passenger.Flight_no = Flight.Flight_no and PNR='{}'".format(pnr)
      cursor.execute(c)
      t=cursor.fetchone()
      #print(t)
      limit="SELECT Available_seats FROM Flight WHERE Flight_no='{}'".format(t[2])
      cursor.execute(limit)
      lim_seat=int(cursor.fetchone()[0])
      #print(lim_seat)
      seats=seats[:lim_seat]
      already_taken_seats = "select seat_no from Passenger where Flight_no='{}'".format(t[2])
      cursor.execute(already_taken_seats)
      seat=cursor.fetchall()
      print("data",seat)
      
      for i in seat:
        try:
         seats.remove(i[0])
        except:
         pass     
    print(seats)     
    return render(request,'checkindetails.html',{'flypnr':t,'seatno':seats})


def seatcheckin(request):
    sepnr=''
    seat_no=''
    if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
  
      for key,value in d.items():
        if key=="sepnr":
                sepnr=value
        if key=="seat":
                seat_no=value
        

      c="UPDATE Passenger set seat_no='{}',checkin_status='yes' WHERE PNR='{}'".format(seat_no,sepnr)
      cursor.execute(c)
      print(c)
      m.commit()
      print(sepnr)
      print(seat_no)
      #t=list(cursor.fetchall())
      #print(t)

      c="Select PNR,concat(Fname, concat(' ', Lname)) AS name,Flight.Flight_no,from_,to_,Arrival,seat_no from Passenger, Flight where Passenger.Flight_no = Flight.Flight_no and PNR='{}' ".format(sepnr)

      cursor.execute(c)
      t=cursor.fetchone()
   
    return render(request,'ticket.html', {'t':t})

    

def stafffwebcheckin(request):
    #if not request.session.get('islogged', False):
     # return render(request,'login_page.html',{'bkmsg':'Please Login to webcheck in'})
    global wpnr,wfn,wln,l
    if request.method=="POST":
      connStr = 'system/password@localhost:1521/xe'
      m = cx_Oracle.connect(connStr)
      cursor=m.cursor()
      d=request.POST
      #m.close()
      for key,value in d.items():
        if key=="pnrno":
                wpnr=value
        if key=="pnrfn":
                wfn=value
        if key=="pnrln":
                wln=value
      c="SELECT * FROM Passenger WHERE PNR='{}' and Fname='{}' and Lname='{}'".format(wpnr,wfn,wln)
      cursor.execute(c)
    
      #m.commit()
      print(c)
      #t=list(cursor.fetchall())
      if not c:
        return render(request,'web_check.html', {'webmsg': 'Invalid credentials'})
      #print(t)
      
    return render(request,'staffwebcheckin.html')