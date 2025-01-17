from django.db import models
import random
from decimal import Decimal 
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import SafeText
from django.conf import settings

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class OtherServices(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Other Services"

class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image=models.ImageField(upload_to='rooms')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    units = models.IntegerField()
    is_available = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, unique=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def get_features(self):
        features=Feature.objects.filter(room=self).all()
        return features
    
    def get_featured_images(self):
        images=RoomFeaturedImage.objects.filter(room=self).all()
        return images

    def get_absolute_url(self):
        return reverse('room_details', kwargs={
            'slug': self.slug,
            })
        
    def get_content(self):
        return format_html(SafeText(self.description))
    
class Feature(models.Model):
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    feature = models.TextField()

class RoomFeaturedImage(models.Model):
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='rooms/featured')
    
class Reservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    guests = models.DecimalField(max_digits=2, decimal_places=0, default=1)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_no = models.SlugField(unique=True, blank=True)
    booked_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name} - #{self.booking_no}"
    
    
    def save(self, *args, **kwargs):
        if not self.booking_no:
            unique_slug = False
            while not unique_slug:
                potential_booking_no = str(random.randint(100000, 999999))
                if not Reservation.objects.filter(booking_no=potential_booking_no).exists():
                    unique_slug = True
            self.booking_no = potential_booking_no       
        super().save(*args, **kwargs)

class Review(models.Model):
    room = models.ForeignKey(Room, related_name='reviews', on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.email} for {self.room.name}"
        
class Accommodation(models.Model):
    room_number = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return f"Room {self.room_number}"
    
class Social(models.Model):
    name=models.CharField(max_length=100)
    link=models.URLField()
    icon = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f'{self.name}'
    
class Contact(models.Model):
    company_name=models.CharField(max_length=225)
    address1=models.CharField(max_length=225)
    address2=models.CharField(max_length=225, blank=True)
    email1=models.CharField(max_length=225)
    email2=models.CharField(max_length=225, blank=True)
    phone1=models.CharField(max_length=225)
    phone2=models.CharField(max_length=225, blank=True)
    phone3=models.CharField(max_length=225, blank=True)
    phone4=models.CharField(max_length=225, blank=True)
    phone5=models.CharField(max_length=225, blank=True)
    
    class Meta:
        verbose_name_plural = 'Contact Information'
        
    def __str__(self):
        return f'Contact Info'

class About(models.Model):
    name=models.CharField(max_length=999)
    about=models.TextField()
    mission=models.TextField(blank=True)
    vision=models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'About Us'
        
    def __str__(self):
        return f'About Us'
    
class Testimonial(models.Model):
    user =models.CharField(max_length=225)
    testimonial=models.TextField()
    role=models.CharField(max_length=100, default='Best Customer')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user
    
class Gallery(models.Model):
    image=models.ImageField(upload_to='gallery')
    caption=models.TextField(blank=True, null=True)
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
    
    class Meta:
        ordering = ["uploaded_at"]
        verbose_name_plural = "Galleries"
    
class Blog(models.Model):
    title=models.CharField(max_length=999)
    image=models.ImageField(upload_to='blogs')
    description=models.CharField(max_length=999, blank=True, null=True)
    content=models.TextField()
    slug = models.SlugField(blank=True, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["created_at"]
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def get_content(self):
        return format_html(SafeText(self.content))

class Activities(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField( blank=True)
    image=models.ImageField(upload_to='activities', blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Activities"
        
class Newsletter(models.Model):
    email=models.CharField(max_length=225)
    
    def __str__(self):
        return self.email
    
class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Privacy Policies'

    def formatted_description(self):
        return format_html(SafeText(self.description))

class TermsOfService(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    def formatted_description(self):
        return format_html(SafeText(self.description))