from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import UserManager

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
)

MARITUL_STATUS_CHOICES = (
    ('SI', 'SINGILE'),
    ('MA', 'MARRIED'),
    ('OT', 'OTHER')
)
class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=255, unique=True, null=True,blank=True,
                                    error_messages={'unique': "Email already used"})
    employe_id= models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True, blank=True)
    maritul_status = models.CharField(max_length=200, null=True, blank=True, choices=MARITUL_STATUS_CHOICES)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'users_user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ["-id"]

    def __str__(self):
        return self.email

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.IntegerField()
    created_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users_otp'
        verbose_name = 'otp'
        verbose_name_plural = 'otps'
        ordering = ["-id"]

    def __str__(self):
        return f'{self.user.email}--{self.otp}'