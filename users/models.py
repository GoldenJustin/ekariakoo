from django.db import models
from django.contrib.auth.models import PermissionsMixin
<<<<<<< HEAD
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
=======
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group, Permission
>>>>>>> origin/main


class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, is_staff=None, password=None):
        if not email:
            raise ValueError('Valid email address is required!')

        if not username:
            raise ValueError('Valid username is required!')

        user = self.model(
<<<<<<< HEAD
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name
        ) 

        user.set_password(password)
        user.save(using = self._db)
=======
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
>>>>>>> origin/main
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
<<<<<<< HEAD
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
=======
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
>>>>>>> origin/main
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
<<<<<<< HEAD
        user.save(using = self._db)
=======
        user.save(using=self._db)
>>>>>>> origin/main
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

<<<<<<< HEAD
=======
    groups = models.ManyToManyField(
        Group,
        related_name='account_set',  # Change this to avoid clash
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='account'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='account_set',  # Change this to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='account'
    )

>>>>>>> origin/main
    USERNAME_FIELD = 'email'  # login using email
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserAccountManager()
<<<<<<< HEAD
    
=======

>>>>>>> origin/main
    class Meta:
        db_table = 'user'
        verbose_name = 'account'
        verbose_name_plural = 'Users'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


<<<<<<< HEAD

class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE) 
    address_line_1 = models.CharField(blank=True, max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=20)
    town = models.CharField(blank=True, max_length=20) 
=======
class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1 = models.CharField(blank=True, max_length=100)
    address_line_2 = models.CharField(blank=True, max_length=100)
    city = models.CharField(blank=True, max_length=20)
    town = models.CharField(blank=True, max_length=20)
>>>>>>> origin/main

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'

    def __str__(self):
        return self.user.first_name
<<<<<<< HEAD
    
=======
>>>>>>> origin/main


class Vendor(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=100)
    shop_name = models.CharField(blank=True, max_length=100)
    location = models.CharField(max_length=100)
    city = models.CharField(blank=True, max_length=20)

    def full_address(self):
        return f'{self.location} {self.city}'

    def __str__(self):
<<<<<<< HEAD
        return self.shop_name
=======
        return self.shop_name
>>>>>>> origin/main
