from django.contrib import admin
from .models import *
admin.site.register(Service)
admin.site.register(OtherServices)
admin.site.register(Testimonial)
# admin.site.register(Accommodation)
admin.site.register(Social)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Gallery)
admin.site.register(Activities)
admin.site.register(Newsletter)
admin.site.register(PrivacyPolicy)
admin.site.register(TermsOfService)

class RoomFeaturedImageInLine(admin.TabularInline):
    model=RoomFeaturedImage
    extra=0

class FeaturesInLine(admin.TabularInline):
    model=Feature
    extra=0

class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display=('name', 'price', 'is_available', 'units')
    inlines = (FeaturesInLine,RoomFeaturedImageInLine,)
admin.site.register(Room, RoomAdmin)

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display=('title', 'created_at', 'updated_at')
admin.site.register(Blog, BlogAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display=('booking_no', 'first_name', 'last_name', 'guests', 'check_in_date', 'check_out_date', 'room')
admin.site.register(Reservation, ReservationAdmin)
