from unicodedata import name
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.schedule, name='schedule'),
    path('schedule', views.schedule, name='schedule'),
    path('booking/<int:schedule_id>', views.booking, name='booking'),
    path('ticketing/<int:schedule_id>', views.ticketing, name='ticketing'),
    path('bookingbyschedule/<int:schedule_id>', views.returnBookingbySc, name='bookingbyschedule'),
    path('printBill', views.printBill, name='printBill'),
    path('cancel', views.cancelBooking, name='cancelBooking'),
    path('cancelTickets/<int:sc_id>', views.cancelTickets, name='cancelTickets'),
    path('cancelreservation/<int:sc_id>', views.cancelReservation, name='cancelReservation'),
    path('time/<int:schedule_id>', views.addtime, name='addtime'),
    path('edituser/<int:user_id>', views.edituser, name='edituser'),
    path('removeuser/<int:user_id>', views.removeuser, name='removeuser'),
    path('close/<int:schedule_id>', views.close, name='close'),
    path('driver', views.registerDriver, name='driver'),
    path('bus', views.registerBus, name='bus'),
    path('terminal', views.registerTerminal, name='terminal'),
    path('route', views.registerRoute, name='route'),
    path('assignroute', views.assignRoute, name='assignroute'),
    path('assigndriver', views.assignDriver, name='assigndriver'),
    path('fares', views.fares, name='fares'),
    path('fares/<int:fare_id>', views.fares, name='fares'),
    path('registerschedule', views.registerSchedule, name='registerschedule'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('import', views.importData, name='import'),
    path('warning', views.warning, name='warning'),
    path('createuser', views.createUser, name='createuser'),
    path('viewusers', views.viewUsers, name='viewusers'),
    path('bookingdetail', views.bookingdetail, name='bookingdetail'),
    path('vouchers', views.vouchers, name='vouchers'),
    path('modifybus/<int:bus_id>', views.modifybus, name='modifybus'),
    path('modifydriver/<int:driver_id>', views.modifydriver, name='modifydriver'),
    path('viewbuses', views.viewbuses, name='viewbuses'),
    path('viewbuses/<int:bus_id>', views.viewbuses, name='viewbuses'),
    path('viewdrivers', views.viewdrivers, name='viewdrivers'),
    path('viewdrivers/<int:driver_id>', views.viewdrivers, name='viewdrivers'),
    path('midtimes', views.midtimes, name='midtimes'),
    path('addtimetosc/<int:schedule_id>', views.addtimetosc, name='addtimetosc'),
    path('viewroutes', views.viewroutes, name='viewroutes'),
    path('viewroutes/<int:route_id>', views.viewroutes, name='viewroutes'),
    path('modifyroute/<int:route_id>', views.modifyroute, name='modifyroute'),
    path('viewmidpoints', views.viewmidpoints, name='viewmidpoints'),
    path('viewmidpoints/<int:mp_id>', views.viewmidpoints, name='viewmidpoints'),
    path('viewterminals', views.viewterminals, name='viewterminals'),
    path('viewterminals/<int:t_id>', views.viewterminals, name='viewterminals'),
    path('modifyterminal/<int:t_id>', views.modifyterminal, name='modifyterminal')
]
