from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from accounts.models import Worker, Booking


def electricians(request):
    obj = Worker.objects.filter(type_of_work='electrician')
    context = {
        'objects': obj
    }
    return render(request, "Electricians.html", context)


def cleaners(request):
    obj = Worker.objects.filter(type_of_work='cleaner')
    context = {
        'objects': obj
    }
    return render(request, "Cleaners.html", context)


def shifters(request):
    obj = Worker.objects.filter(type_of_work='shifter')
    context = {
        'objects': obj
    }
    return render(request, "Shifters.html", context)


def workers(request):
    obj = Worker.objects.filter(type_of_work='worker')
    context = {
        'objects': obj
    }
    return render(request, "Workers.html", context)


def plumbers(request):
    obj = Worker.objects.filter(type_of_work='plumber')
    context = {
        'objects': obj
    }
    return render(request, "Plumbers.html", context)


def painters(request):
    obj = Worker.objects.filter(type_of_work='painter')
    context = {
        'objects': obj
    }
    return render(request, "Painter.html", context)


def booking(request):
    # obj = Worker.objects.filter(type_of_work='worker')
    # context = {
    #     'objects': obj
    # }
    return render(request, "booking.html")


def request(request):
    obj = Booking.objects.filter(worker_id=request.session['worker_id'])
    context = {
        'objects': obj
    }
    return render(request, "Notifications.html", context)


@csrf_protect
def booking_request(request):
    obj = Booking.objects.all()
    context = {
        'objects': obj
    }
    if request.POST:
        booking_id = request.POST.get('booking_id')
        update_booking = obj.get(id=booking_id)
        update_booking.status = request.POST.get('status')
        update_booking.save()

    return render(request, "Notifications.html", context)
