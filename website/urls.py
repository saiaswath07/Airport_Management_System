"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from signup.views import signaction
from login.views import loginaction
from staff_login.views import *
from contactus.views import *
from login.views import *
from booking.views import bookingaction
from searchflight.views import searchflightaction
from passenger.views import passengeraction
from payment.views import paymentaction
from booking.views import dumaction
from payment.views import successaction
from django.conf.urls.static import static
from booking.views import webcheckinaction
from booking.views import extractflytno
from webcheckin.views import webcheckinaction
from webcheckin.views import checkindetailsaction
from webcheckin.views import seatcheckin
from security_flight.views import securitystarusaction
from ticket.views import ticketaction
from security_flight.views import securityloginaction
from webcheckin.views import stafffwebcheckin 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signaction),
    path('login/',loginaction),
    path('staff_login/',staffloginaction),
    path('contactus',contactusaction),
    path('aboutus',aboutusaction),
    path('booking',bookingaction),
    path('searchflight',searchflightaction),
    path('passenger',passengeraction),
    path('payment',paymentaction),
    path('dum',dumaction),
    path('success',successaction),
    path('webcheckin',webcheckinaction),
    path('extractno',extractflytno),
    path('webcheckin',webcheckinaction),
    path('checkindetails',checkindetailsaction),
    path('seatcheck',seatcheckin),
    path('security',securitystarusaction),
    path('ticket',ticketaction),
    path('logout/',logout),
    path('signup_login/',signup_login),
    path('addflight',addflightaction),
    path('manageflight',manageflightaction),
    path('security_login',securityloginaction),
    path('queries',passqueries),
    path('staffwebcheckin',stafffwebcheckin)

   














]
