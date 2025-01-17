from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views import View
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
import json
from django.contrib import messages
from .utils import is_room_available
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
# import zeptomail

def index(request):
    about=About.objects.first()
    services=Service.objects.all()
    blogs=Blog.objects.all()[:3]
    context ={
        'about':about,
        'services':services,
        'blogs':blogs,
    }
    return render(request, 'index.html', context)

def about(request):
    other_services=OtherServices.objects.all()
    about=About.objects.first()
    context ={
        'other_services':other_services,
        'about':about,
    }
    return render(request, 'about.html', context)

def gallery(request):
    images=Gallery.objects.all()
    context ={
        'images':images,
    }
    return render(request, 'gallery.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Gather form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            email_address = form.cleaned_data['email']
            message = form.cleaned_data['message']


            subject="New Contact Form Submission"
            html_content = render_to_string('mail/admin-email-sent.html', {
                'first_name': first_name,
                'last_name': last_name,
                'phone': phone,
                'email': email_address,
                'message': message
                })
            email = EmailMessage(
                subject,
                html_content,
                from_email=settings.DEFAULT_FROM_EMAIL,  # Sender's email
                to=['info@thibadamresort.org'],  # List of recipient email addresses
                
            )
            email.content_subtype = "html"  # Ensure the email is treated as HTML
            email.send()
            
            # Send confirmation email to user

            subject="Thank You for Contacting Us"
            html_content = render_to_string('mail/email-sent.html', {
                'first_name': first_name,
                'last_name': last_name,
                })
            user_email = EmailMessage(
                subject,
                html_content,
                from_email=settings.DEFAULT_FROM_EMAIL,  # Sender's email
                to=[email_address],  # List of recipient email addresses
                
            )
            user_email.content_subtype = "html"  # Ensure the email is treated as HTML
            user_email.send()
            
            messages.success(request, "Email has been sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "Email has not been sent. Try again!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def blog(request):
    return render(request, 'blog.html')

def services(request):
    services=Service.objects.all()
    activities=Activities.objects.all()
    context ={
        'services':services,
        'activities':activities,
    }
    return render(request, 'services.html', context)

def rooms(request):
    rooms=Room.objects.all()
    
    context ={
        'rooms':rooms,
    }
    return render(request, 'rooms.html', context)

class RoomDetailView(DetailView):
    def get(self, request, slug):
        """Handles GET requests to display room details."""
        room = get_object_or_404(Room, slug=slug)
        reviews = room.reviews.all()  # Fetch reviews for the room
        form = ReviewForm() 
        room_options = range(1, int(room.units) + 1)
        featured_images = room.get_featured_images()
        available_rooms = Room.objects.filter(is_available=True)
        available_units = room.units
        context = {
            'room': room,
            'reviews': reviews,
            'form': form,
            'featured_images': featured_images,
            'available_units': available_units,
            'room_options': room_options,
        }
        return render(request, 'room-details.html', context)
    

    def post(self, request, slug):
        """Handles POST requests to add a review."""
        room = get_object_or_404(Room, slug=slug)
        reviews = room.reviews.all()
        form = ReviewForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if room.reviews.filter(email=email).exists():
                return render(request, 'room-details.html', {
                    'room': room,
                    'reviews': reviews,
                    'form': form,
                    'error': 'A review with this email already exists for this room.',
                })
            review = form.save(commit=False)
            review.room = room
            review.save()
            return redirect('room_detail', slug=slug)
        return render(request, 'room-details.html', {
            'room': room,
            'reviews': reviews,
            'form': form,
        })
        
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            room = form.cleaned_data['room']
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            guests = form.cleaned_data['guests']
            
            available = is_room_available(room, check_in_date, check_out_date)

            if available:
                reservation = Reservation.objects.create(
                    first_name=request.POST.get('first_name'),
                    last_name=request.POST.get('last_name'),
                    email=request.POST.get('email'),
                    guests=guests,
                    check_in_date=check_in_date,
                    check_out_date=check_out_date,
                    room=room,
                )
                reservation.save()
                user_subject = "Booking Confirmation"
                user_context = {
                    'first_name': reservation.first_name,
                    'last_name': reservation.last_name,
                    'booked_at': reservation.booked_at,
                    'room_name': reservation.room.name,
                    'guests':reservation.guests,
                    'price': reservation.room.price,
                }
                user_message = render_to_string('mail/booking-confirmed.html', user_context)
                user_email = EmailMessage(
                    subject=user_subject,
                    body=user_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[reservation.email],
                )
                user_email.content_subtype = "html"
                user_email.send()

                # Send email to the admin
                admin_subject = "New Booking Notification"
                admin_context = {
                    'first_name': reservation.first_name,
                    'last_name': reservation.last_name,
                    'booking_no': reservation.booking_no,
                    'check_in_date': reservation.check_in_date,
                    'check_out_date': reservation.check_out_date,
                    'guests':reservation.guests,
                    'price': reservation.room.price,
                }
                admin_message = render_to_string('mail/admin-booking-confirmed.html', admin_context)
                admin_email = EmailMessage(
                    subject=admin_subject,
                    body=admin_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[settings.ADMIN_EMAIL],
                )
                admin_email.content_subtype = "html"
                admin_email.send()

                message = f"Booking successful! Your reservation number is #{reservation.booking_no}. Contact us for more information."
                status=200
                return render(request, 'success.html', {'message': message,  'status':status})
            else:
                message = f"Booking unsuccessful! Contact us for more information."
                status=404
                return render(request, 'success.html', {'message': message,  'status':status})

    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})


def newsletter(request):
    if request.method == 'POST':
        form = NewsLetterSubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not Newsletter.objects.filter(email=email).exists():
                newsletter = Newsletter(email=email)
                newsletter.save()
                messages.success(request, 'Thank You For Subscribing To Our Newsletter!')
            else:
                messages.error(request, 'You are already subscribed to the newsletter.')
        else:
            messages.error(request, 'Invalid email address. Please try again.')
    return redirect('index')

def check_room_availability(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            room = form.cleaned_data['room']
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']

            available = is_room_available(room, check_in_date, check_out_date)
            status=None
            
            if available:
                message = f"The <span class='text-decoration-underline'>{room.name}</span> is available from {check_in_date} to {check_out_date}."
                status=200
            else:
                message = f"The <span class='text-decoration-underline'>{room.name}</span> is not available for the selected dates."
                status=404
            return render(request, 'availability_result.html', {'message': message, 'status':status})

    else:
        form = AvailabilityForm()

    return render(request, 'check_availability.html', {'form': form})


def privacy(request):

    policies = PrivacyPolicy.objects.all()

    context = {
        'policies': policies,
    }
    
    return render(request, 'privacy.html', context)

def terms(request):
    terms = TermsOfService.objects.all()

    context = {
        'terms': terms,
    }
    return render(request, 'terms.html', context )

def test(request):
    return render(request, 'mail/admin-email-sent.html')