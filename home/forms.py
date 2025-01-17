from django import forms
from .models import Review, Room
from django.utils import timezone

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['email', 'rating', 'comment']
        widgets = {
            'name': forms.EmailInput(attrs={'placeholder': 'Your email'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email'}),
            'rating': forms.Select(choices=[(i, str(i)) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your review'}),
        }


class NewsLetterSubscriptionForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': ' width-100% height-100% form-control',
            'id': 'email',
            'name': 'email',
            'placeholder': 'Enter Your Email',
        }),label=""
    )

class AvailabilityForm(forms.Form):
    today = timezone.now().date()
    
    room = forms.ModelChoiceField(queryset=Room.objects.all(), required=True, widget=forms.Select(attrs={
        'class': 'select-option',
        'id': 'room',
    }))
    check_in_date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'date-input',
        'id': 'date-in',
        'type': 'date',
        'min': today, 
    }))
    check_out_date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'date-input',
        'id': 'date-out',
        'type': 'date',
        'min': today, 
    }))

    guests = forms.IntegerField(
        min_value=1,
        max_value=20,
        widget=forms.NumberInput(attrs={
            'class': 'select-option',
            'id': 'guest',
            'placeholder': '1 Adult',
            'step': 1,
            'max': 20, 
        }))
    
class BookingForm(forms.Form):
    today = timezone.now().date()
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First name',
            'id': 'first_name',
        })
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last name',
            'id': 'last_name',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'E-mail Address',
            'id': 'email',
        })
    )
    room = forms.ModelChoiceField(queryset=Room.objects.all(), required=True, widget=forms.Select(attrs={
        'class': 'select-option',
        'id': 'room',
    }))
    check_in_date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'date-input',
        'id': 'date-in',
        'type': 'date',
        'min': today, 
    }))
    check_out_date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'date-input',
        'id': 'date-out',
        'type': 'date',
        'min': today, 
    }))

    guests = forms.IntegerField(
        min_value=1,
        max_value=20,
        widget=forms.NumberInput(attrs={
            'class': 'select-option',
            'id': 'guest',
            'placeholder': '1 Adult',
            'step': 1,
            'max': 20, 
    }))

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="First name", widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    last_name = forms.CharField(max_length=100, label="Last name", widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    phone = forms.CharField(max_length=15, label="Phone", widget=forms.TextInput(attrs={'class': 'form-control', 'required': True}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'example@email.com'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'required': True}))
