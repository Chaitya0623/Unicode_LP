from asyncio.windows_events import NULL
from email.policy import default
from tkinter import Image
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.


    
class UserManager(BaseUserManager):

    def create_user(self,email,password=None,is_active=True,is_staff=False,is_admin=False):

        if not email:

            raise ValueError("Users must have email")

        

        if not password:

            raise ValueError("Users must have password")

        user_obj=self.model(

            email=self.normalize_email(email)

        )

        user_obj.staff=is_staff

        user_obj.admin=is_admin

        user_obj.active=is_active

        user_obj.set_password(password)

        user_obj.save(using=self._db)

        return user_obj

    

    def create_staffuser(self,email,password=None):

        user=self.create_user(

            email,

            password=password,

            is_staff=True

            )

        return user

    

    def create_superuser(self,email,password=None):

        user=self.create_user(

            email,

            password=password,

            is_staff=True,

            is_admin=True

        )

        return user




class MyUser(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    # full_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True) #can login
    staff = models.BooleanField(default=False) #staff user non superuser
    admin = models.BooleanField(default=False) #superuser
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email' #username
    REQUIRED_FIELDS=[]
    objects=UserManager()
    #email and password are required for default
    def __str__(self):
        return self.email
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
        
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_active(self):
        return self.active
        
class User(models.Model):
    Name = models.CharField(max_length=20)
    Description = models.TextField()
    Married = models.BooleanField(blank=True)
    Birthday = models.DateTimeField()
    Image = models.ImageField(null=True, blank=True, upload_to='static/')
    email = models.ForeignKey(MyUser, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return self.Name

class Foreign(models.Model):
    User = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    Age = models.IntegerField(default=NULL)
    
    def __str__(self):
        return self.Age

# class Profile(models.Model):
#     user = models.OneToOneField(MyUser)