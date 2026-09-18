from django.shortcuts import render, redirect, get_object_or_404
from celebrities.models import Celebrity
from .models import Booking
from .forms import BookingForm


def booking_list(request):
    return render(request, 'bookings/list.html')


def booking_create(request, celebrity_slug):
    celebrity = get_object_or_404(Celebrity, slug=celebrity_slug)

    # Block if unavailable
    if celebrity.status == 'unavailable':
        return redirect('celebrities:detail', slug=celebrity_slug)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.celebrity = celebrity
            booking.save()
            return redirect('bookings:success', booking_id=booking.id)
    else:
        form = BookingForm()

    context = {
        'page_title'       : f'Book {celebrity.name} | LuminaStars',
        'meta_description' : f'Submit a booking request for {celebrity.name} via LuminaStars.',
        'celebrity'        : celebrity,
        'form'             : form,
    }
    return render(request, 'bookings/create.html', context)


def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    context = {
        'page_title' : 'Booking Received | LuminaStars',
        'booking'    : booking,
    }
    return render(request, 'bookings/success.html', context)