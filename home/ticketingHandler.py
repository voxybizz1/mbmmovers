from home.models import Refund, Schedule, Passenger, Tickets, Fares, UserofTerminal
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Count
import json

class TicketingHandler():
    @staticmethod
    def returnTicketing(request, schedule_id):
        schedule = Schedule.objects.filter(id=schedule_id)[0]
        if request.method == "POST":
            try:
                data = request.POST
                passenger = Passenger.objects.filter(cnic = data['inputCnic'])
                faresRoute = Fares.objects.get(id=int(data['inputRoute']))
                ps = None
                if passenger:
                    passenger.update(phone = data['inputContact'])
                    ps = passenger[0]
                else:
                    passenger = {'name' : data['inputPasName'], 'gender' : int(data['inputBookedbyGender']), 'phone' : data['inputContact'], 'cnic' : data['inputCnic']}
                    ps = Passenger(name=passenger['name'], gender=passenger['gender'], phone=passenger['phone'], cnic=passenger['cnic'])
                    ps.save()
                seats = [int(i) for i in data['inputSeats'].split(',')]
                genders = [int(i) for i in data['inputGenders'].split(',')]
                fare = Fares.objects.get(id=int(data['inputRoute']))
                for i in range(len(seats)):
                    tk = Tickets(voucher = data['inputVoucher'], schedule = schedule, discount = data['inputDiscount'], source = faresRoute.source, destination = faresRoute.destination, seat_no = seats[i], fare= fare,bookedby = ps, gender = genders[i], status = 2, type = 1, issuedby = request.user)
                    tk.save()
                messages.success(request, 'Tickets has been purchased successfully!')
            except Exception as e:
                messages.warning(request, e)
        dt = None
        try:
            tickets = Tickets.objects.filter(schedule=schedule_id)
            uterminal = UserofTerminal.objects.get(user=request.user)
            fares = Fares.objects.filter(route=schedule.route_assg_bus.route, service_type= schedule.route_assg_bus.bus.service_type, source=uterminal.terminal)
            seating = {}
            for i in tickets.values():
                fare = Fares.objects.get(id=i['fare_id'])
                if fare.destination.id == uterminal.terminal.id:
                    continue
                bookedincity = fare.source.city
                destcity = fare.destination.city
                gender = i['gender']
                status = i['status']
                seating[i['seat_no']] =  {'gender':gender, 'status':status, 'bookedincity':bookedincity, 'destcity': destcity}
            deptime = None
            if schedule.mid_dept:
                mpoints = json.loads(schedule.mid_dept)
                if str(uterminal.terminal.id) in mpoints:
                    deptime = mpoints[str(uterminal.terminal.id)]
            result = {'schedule': schedule, 'deptime': deptime, 'seating': seating, 'range': range(schedule.route_assg_bus.bus.seating_capacity), 'fares': fares}
            dt = {'request': request, 'result': result}
        except Exception as e:
            dt = {'request': request, 'result': None}
            messages.warning(request, e)
        return dt
    
    @staticmethod
    def cancelTickets(request, sc_id):
        tickets = None
        try:
            schedule = Schedule.objects.get(id=sc_id)
            uterminal = UserofTerminal.objects.get(user=request.user)
            tickets = Tickets.objects.filter(schedule=schedule, source=uterminal.terminal, status=2)
        except Exception as e:
            messages.warning(request, e.args)
        if request.method == "POST":
            try:
                tk_ids = dict(request.POST)
                for i in tk_ids['ticket']:
                    tk = Tickets.objects.get(id=i)
                    refund_query = Refund(passenger=tk.bookedby, schedule=tk.schedule, seats = tk.seat_no, amount = tk.fare.fare)
                    refund_query.save()
                    tk.delete()
                tickets = Tickets.objects.filter(schedule=schedule, status=2)
                if not tickets:
                    tickets = None
                messages.success(request, 'Tickets cancelled successfully!')
            except Exception as e:
                messages.warning(request, e)
        return {'request': request, 'tickets':tickets}
    