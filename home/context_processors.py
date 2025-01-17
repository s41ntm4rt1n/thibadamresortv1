from .models import *
from .forms import NewsLetterSubscriptionForm, AvailabilityForm

def contact(request):
    contact=Contact.objects.all().first()
    if contact:
        return {"contact": contact}
    return None


def newsletter_subscription_form(request):
    return {'newsletter_form': NewsLetterSubscriptionForm()}

def room_checker_form(request):
    return {'form': AvailabilityForm()}