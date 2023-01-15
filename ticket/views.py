from django.shortcuts import render
import cx_Oracle
# Create your views here.
def ticketaction(request):
    pnr=request.session['pnr']
    #print(pnr)  
    connStr = 'system/password@localhost:1521/xe'
    m = cx_Oracle.connect(connStr)
    cursor=m.cursor()
    
    c="Select PNR,concat(Fname, concat(' ', Lname)) AS name,Flight.Flight_no,from_,to_,Arrival,seat_no from Passenger, Flight where Passenger.Flight_no = Flight.Flight_no and PNR='{}' ".format(pnr)



    #print("****************************************************************************",c)

    cursor.execute(c)
    t=cursor.fetchone()
    print(pnr)
    print(t)

    #m.commit() 

    

    return render(request,'ticket.html',{'t':t})