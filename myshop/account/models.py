from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('user'), on_delete=models.CASCADE)
    # date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(_('photo'), upload_to='users/%Y/%m/%d/', blank=True)
    phone_number = PhoneNumberField(_('phone number'), null=True, blank=True)
    
    def __str__(self):
        return f'Profile of {self.user.username}'
