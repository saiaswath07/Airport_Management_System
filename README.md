# Airport_Management_System
Airport Management System  using html,css,javascript,Django and oracle 11g as database 


Airports have become one of the most trafficked places by passengers. There are many operations to be handled by passengers and airport staff once we enter the airport. So, we need a system to handle such a vast number of passengers, flights, security, and staff in the airport. In this project, we going to maintain the details of passengers, security staff, and flight staff in an airport and the information about the personal details of the passengers and their bookings. The passengers can download their flight tickets and can check their other flight details. The details of the security staff and the flight staff for each flight are also stored they can log in and perform their respective work such as checking in passengers. 


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
MODULES OF THE PROJECT

Database: Oracle 11g 
DBMS (Database Management System) is a software that helps to create and manage databases easily 
and efficiently. An RDBMS is a DBMS that follows the relational model. In other words, these 
systems use a relational model to store data. They store data in tables, which are connected to each 
other. Oracle is one such RDBMS

Frontend and backend connection: Python Framework Django
Django is a back-end server-side web framework. Django is free, open source and written in Python.
Django makes it easier to build web pages using Python.

Editor: vs code 
Visual Studio Code (famously known as VS Code) is a free open-source text editor by Microsoft. 
Although the editor is relatively lightweight, it includes some powerful features that have made VS 
Code one of the most popular development environment tools in recent times

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ER Diagram :
![er diagram](https://user-images.githubusercontent.com/67650775/212552713-8504087e-1f02-48c9-b3f3-ccfd62c55126.jpeg)

Work flow of the website :

![workflow](https://user-images.githubusercontent.com/67650775/212552869-5f47806d-73dc-4e73-82c3-dfccedd7db1a.png)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Step 1:Download oracle 11g for backend.
link to download oracle 11g:https://drive.google.com/file/d/1BdcGM9NhoPLzOTFKQZbwO3FPM8E-WmBd/view

Step 2:open vs code or any other terminal and run the below commands 
pip install cx_oracle
pip install django

step 3:Download sql developer to access backend to create tables and perform operations.
link to download oracle 11g:https://www.oracle.com/database/sqldeveloper/technologies/download/

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sql tables :

TABLES(Unfiltered):

1) Passenger(PNR, Fname, Lname, Gender, Nationality, Security Status, check-in status)
2) Passenger_Ph(PNR, Phone no)
3) webVisitor(Cookie_no, ip addr, Loc, email id, mobile no)
4) webVisitorCard(Cookie_no, card no, card name, cvv)
5) Flight(Flight no, Flight Name, From, To, Arrival, Departure, Available seats)
6) Staff(Staffid, FFIName, LFIName, Area, PIN)
7) Staff_pn(Staffid,phone no)
8) Security Officer(id, SFName, SLName, SArea, SPIN,Gate no)
9) Security Officer_pn(id,sec phone no)
10) Passenger(PNR, Fname,Lname,Gender,Nationality,Security Status,check-in 
status,Flight no)
11) Passenger(PNR, Fname,Lname,Gender,Nationality,Security Status,check-in 
status,Staffid)
12) Passenger(PNR, Fname,Lname,Gender,Nationality,Security Status,check-in status,sec id)
13) Flight(Flight no, Flight Name, From, To, Arrival, Departure, Available seats,Staffid)
14) webVisitor(Cookie_no, ip addr, Loc, email id, mobile no,Staffid)
15) webVisitorFlight(Flight no, cookie id)
16) webVisitorFlight(Flight no, cookie id, tckt no


TABLES(Filtered):

1) Passenger(PNR, Fname, Lname, Gender, Nationality, Security Status, check-in 
status,flightno, staffid, sec_id) --- fk: flightno, staffid, sec id
2) Passenger_Ph(PNR, Phone no)
3) webVisitor(Cookie_no, ip addr, Loc, email id, mobile no,staff id) fk: staffid
4) webVisitorCard(Cookie_id, card no, card name, cvv, exp_date)
5) Flight (Flight no, Flight Name, From, To, Arrival, Departure, Available seats,Price, 
staff id) fk: staffid
6) Staff(Staffid, FFIName, LFIName, Area, PIN)
7) Staff_pn(Staffid,phone no)
8) Security Officer(sec_id, SFName, SLName, SArea, SPIN,Gate no)
9) Security Officer_pn(sec_id,sec_phone no)
10) webVisitorFlight(Flight no, cookie_ id, tckt_no

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Sql queries:

CREATE TABLE usr(firstname varchar(50),lastname varchar(50),email varchar(100) UNIQUE,passsword varchar(50),conpassword varchar(50));

CREATE TABLE Security_Officer(sec_id varchar(10) PRIMARY KEY, SFName varchar(30),SLName varchar(30), SArea varchar(255), SPIN varchar(7),Gate_no varchar(10),email varchar(100),passsword varchar(100));

CREATE TABLE Security_Officer_ph(sec_id varchar(10),sec_phone_no varchar(10),CONSTRAINT security_ph PRIMARY KEY(sec_id,sec_phone_no));
ALTER TABLE Security_Officer ADD passsword varchar(100)

INSERT INTO Security_officer VALUES ('sec01','nandi','reddy','hyd','560025','G01');
SELECT * FROM Security_Officer_ph
INSERT INTO Security_officer_ph VALUES ('sec01','9963249944');


SELECT * FROM Security_Officer where email='kiasec@gmail.com' and passsword='12345'

CREATE TABLE contactus(email VARCHAR(100),name VARCHAR(50),country VARCHAR(50),phno VARCHAR(10));
SELECT * FROM contactus

CREATE TABLE Staff(Staff_id varchar(20) PRIMARY KEY, FFIName varchar(30), LFIName varchar(30), Area varchar(255), PIN NUMBER(7));
ALTER TABLE staff ADD passsword varchar(100)
INSERT INTO staff VALUES('s01','rithivika','alapati','hyd',560016);
INSERT INTO staff VALUES('s02','kiara','advani','mum',560017);
INSERT INTO staff VALUES('s03','nandu','reddy','bng',560018);
INSERT INTO staff VALUES('s04','andana','sree','raj',560019);
INSERT INTO staff VALUES('s05','sai','aswath','bng',560020);
INSERT INTO staff VALUES('s06','team','25','bng',560020,'team25@gmail.com','team25');
SELECT * FROM staff_ph

CREATE TABLE Staff_ph(Staff_id  varchar(20) ,phoneno  varchar(10))
INSERT INTO staff_ph VALUES('s06','6364268505')

SELECT * FROM staff



ALTER SESSION SET NLS_TIMESTAMP_FORMAT  = 'YYYY-MM-DD HH24:MI:SS'

ALTER TABLE Flight ADD deleted VARCHAR(1);
UPDATE Flight SET deleted='n'

CREATE TABLE Flight(Flight_no varchar(30) PRIMARY KEY,Flight_name varchar(30),from_ varchar(20),to_ varchar(20),Arrival TIMESTAMP,Departure TIMESTAMP,Available_seats varchar(50),price varchar(100),Staff_id varchar(20) REFERENCES Staff(Staff_id));
INSERT INTO  Flight VALUES('E7037','INDIGO','Bangalore','Delhi','2022-01-10 10:00:00','2022-01-10 12:00:00',20,5000,'s01');
INSERT INTO  Flight VALUES('E7038','INDIGO','Bangalore','Hyderabad','2022-01-11 12:00:00','2022-01-11 3:00:00',15,7000,'s02');
INSERT INTO  Flight VALUES('B0731','AIRWAYS','Bangalore','Delhi','2022-12-11 8:00:00','2022-12-11 9:00:00',10,17000,'s03');
INSERT INTO  Flight VALUES('B0721','JETWAYS','Bangalore','Chennai','2022-12-13 12:00:00','2022-12-13 2:00:00',5,19000,'s04');
INSERT INTO  Flight VALUES('F0621','AIRWAYS','Bangalore','Goa','2022-12-14 4:00:00','2022-12-14 6:15:00',12,12000,'s05');
INSERT INTO  Flight VALUES('F0622','AIRASIA','Bangalore','Vizag','2022-12-15 4:00:00','2022-12-15 5:15:00',22,14000,'s02');
INSERT INTO  Flight VALUES('flall','INDIGO','Bangalore','Hyderabad','2022-12-21T21:40','2022-12-20T21:36',1,5000,'s01');
INSERT INTO  Flight VALUES('flaall','INDIGO','Bangalore','Hyderabad','2022-12-21 21:40','2022-12-20 21:36',1,5000,'s01');
INSERT INTO  Flight VALUES('zflall','INDIGO','Bangalore','Hyderabad','2022-12-23 21:00','2022-12-23 20:59',1,10,'s01');
INSERT INTO  Flight VALUES('E7012','INDIGO','Bangalore','Hyderabad',TO_TIMESTAMP('2022-12-18 22:27'),TO_TIMESTAMP('2022-12-18 22:27'),1,5000,'s01')
SELECT * FROM Flight 
DELETE FROM Flight WHERE Flight_no='zflall' ;


SELECT *  FROM Flight WHERE TO_DATE(Arrival) AS  Arrival;

select TO_DATE() from Flight;


select * FROM Flight WHERE CONVERT(VARCHAR(10),Arrival) = '10-JAN-2022'                     WHERE from_=bangalore and to_=Delhi
select to_char(cast(Arrival as date),'DD-MM-YYYY'), from_,to_ from Flight WHERE from_='Bangalore' and to_='Delhi' ;

Select TRUNC(Arrival) FROM Flight;

select * FROM Flight WHERE TRUNC(Arrival)='2022-01-10' and from_='Bangalore' and to_='Delhi' ;

select * FROM Flight WHERE to_char(cast(Arrival as date),'YYYY-MM-DD')='2022-01-10' and from_='Bangalore' and to_='Delhi' ;

select dbms_random.string('X', 6) str from dual;


CREATE TABLE Security_Officer(sec_id varchar(10) PRIMARY KEY, SFName varchar(30),SLName varchar(30), SArea varchar(255), SPIN varchar(7),Gate_no varchar(10));
INSERT INTO Security_officer VALUES ('sec01','nandi','reddy','hyd','560025','G01');

INSERT INTO vehicle(vehicle_id, VEHICLE_NAME) SELECT vehicle_id, vehicle_name from employee where Vehicle_name = 'Lexus';INSERT INTO Passenger(PNR,Fname,Lname,Gender,Nationality,Security_Status,checkin_status,checkin_status,Flight_no,staff_id,sec_id) 
SELECT PNR,Fname,Lname,Gender,Nationality,Security_Status,checkin_status,checkin_status,Flight_no,staff_id,sec_id  from  Passenger 
where (PNR=select dbms_random.string('X', 6) str from dual,Fname='sai',Lname='aswath',Gender='Male',Nationality='Indian',Security_Status='yes',checkin_status='yes',Flight_no='B0731',staff_id='s01',sec_id='sec01')


CREATE TABLE Passenger(PNR varchar(20) PRIMARY KEY,Fname varchar(30),Lname varchar(30),Gender varchar(10),Nationality varchar(10),Security_Status varchar(10),checkin_status varchar(10),Flight_no varchar(30),staff_id varchar(20),sec_id varchar(10), FOREIGN KEY(Flight_no) REFERENCES Flight(Flight_no), FOREIGN KEY(staff_id) REFERENCES Staff(Staff_id),FOREIGN KEY(sec_id) REFERENCES Security_Officer(sec_id));
INSERT INTO Passenger VALUES('6387W0','sai','aswath','Male','Indian','yes','yes','E7037','s01','sec01','2C');
SELECT * FROM Passenger
SELECT * FROM Passenger WHERE PNR='XZ2S2J' and Fname='sai' and Lname='aswath'

SELECT * FROM Passenger WHERE Flight_no='E7037'

select seat_no from Passenger where Flight_no='E7037'


INSERT INTO Passenger VALUES('XZ2S2J','sai','aswath','Male','Indian','yes','yes','E7037','s01','sec01')

ALTER SESSION SET NLS_DATE_FORMAT='YYYY-MM';
ALTER TABLE Passenger ADD seat_no VARCHAR(10)


CREATE TABLE Webvisitor_card(Cookie_no varchar(10)PRIMARY KEY,card_no varchar(20),card_name varchar(30),cvv varchar(5),exp_date DATE);
INSERT INTO Webvisitor_card VALUES('ck7526','0000-1236-1236-1235','sai','235','2022-04')
INSERT INTO Webvisitor_card VALUES('ck5022','9632-9632-3654-6324','sdrtfyguhijokjiuhgyftdr','636','2022-11')
INSERT INTO Webvisitor_card VALUES('ck9426','0000-1236-1236-1235','sai','235','2022-04')
INSERT INTO Webvisitor_card VALUES('ck9496','0000-1236-1236-1235','sai','235','2022-04')
INSERT INTO Webvisitor_card VALUES('ck49426','0000-1236-1236-1235','sai','235','2022-10')
INSERT INTO Webvisitor_card VALUES('ck46426','0000-1236-1236-1235','sai','235',TO_DATE('1989-12','YYYY-MM'))

SELECT * FROM Webvisitor_card

SELECT * FROM Flight NATURAL JOIN Passenger;
Select PNR,concat(Fname, concat(' ', Lname)),Flight.Flight_no,from_,to_,Arrival from Passenger, Flight where Passenger.Flight_no = Flight.Flight_no 
XZ2S2J
SELECT * FROM Passenger WHERE Flight_no='E7037'
UPDATE Passenger set Security_Status='no'


CREATE TABLE Passenger_ph(PNR varchar(20),phone_no varchar(10),CONSTRAINT passenger_ph_no PRIMARY KEY(PNR,phone_no));
INSERT INTO  Passenger_ph VALUES('','')
SELECT * FROM Passenger_ph

CREATE TABLE staff_ph(Staff_id varchar(10), phone_no varchar(10),CONSTRAINT staff_ph_no PRIMARY KEY(Staff_id,phone_no));
INSERT INTO staff_ph('s01','9448825994',)

SELECT seat_no FROM Passenger WHERE PNR=''

UPDATE Passenger set seat_no='4D',checkin_status='yes' WHERE PNR='AI1QW8'

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
HOW TO LAUNCH THE WEBSITE 

Step 1 : Open vs code and run python manager.py runserver
Step2 : Go to any Browser and launch http://localhost:8000/login
Step3 : Login to passenger and signup to book the flight  and web check-in
Step 4 : Login to staff to add flights , manage flights and to check passenger queries
Step5 : Login to security and to do security check-up

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
outputs:

![image](https://user-images.githubusercontent.com/67650775/212553678-3c51aeee-b945-4d6a-ab2c-43f205ac9db6.png)

![image](https://user-images.githubusercontent.com/67650775/212553697-16516861-2587-4a03-a123-92b70e46bd45.png)

![image](https://user-images.githubusercontent.com/67650775/212553704-06485f2c-33f9-4d68-a4f4-2a89e07eba40.png)

![image](https://user-images.githubusercontent.com/67650775/212553709-40c73415-a96e-4464-878c-7573656fb2b1.png)

![image](https://user-images.githubusercontent.com/67650775/212553711-9b6b8ef0-57e3-4091-85ce-bd7aca558a0d.png)

![image](https://user-images.githubusercontent.com/67650775/212553714-24639eae-bb3e-4057-a8f8-3191c3059501.png)

![image](https://user-images.githubusercontent.com/67650775/212553725-5cb2bb85-1f3e-4fb9-8fae-bc522ea510cd.png)

![image](https://user-images.githubusercontent.com/67650775/212553742-bc870a4a-2a73-4c8b-8794-f748c68632fb.png)

![image](https://user-images.githubusercontent.com/67650775/212553751-1af0b526-9021-466f-bca4-e3e05a4de8d0.png)

![image](https://user-images.githubusercontent.com/67650775/212553759-49d23b07-b636-4888-b793-a6792f6c11c3.png)









