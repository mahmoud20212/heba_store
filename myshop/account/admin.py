from django.contrib import admin
from .models import Profile
from django.utils.html import format_html
from phonenumber_field.phonenumber import PhoneNumber

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number_display')
    search_fields = ('user__username', 'phone_number')

    def phone_number_display(self, obj):
        if isinstance(obj.phone_number, PhoneNumber):
            return format_html('<a href="tel:{}">{}</a>', obj.phone_number.as_e164, obj.phone_number.as_e164)
        return "No phone number"
    
    phone_number_display.short_description = 'Phone Number'
