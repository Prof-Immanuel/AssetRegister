from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, unique=True)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    owner_phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.item_name} ({self.serial_number})"


class StolenItem(models.Model):
    item_name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, unique=True)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20)
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} ({self.serial_number}) - {self.brand}"


# Custom User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError("Phone number is required")
        user = self.model(phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password):
        user = self.create_user(phone, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

# Custom User Model
class CustomUser(AbstractBaseUser):
    phone = models.CharField(max_length=15, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()
    
     # Permissions Methods
    def has_perm(self, perm, obj=None):
        """Return whether the user has a specific permission."""
        return self.is_active  # You can customize the permission logic

    def has_module_perms(self, app_label):
        """Return whether the user has permissions for a specific app."""
        return self.is_active  # You can customize the module permission logic

    @property
    def is_staff(self):
        return self.is_staff

  

    USERNAME_FIELD = 'phone'
    
    

    def __str__(self):
        return self.phone