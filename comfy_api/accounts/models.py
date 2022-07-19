from django.db import models
from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth.models import (AbstractUser, BaseUserManager)
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, username, email,phone_number=None, full_name=None, gender=None, profile_url=None, reset_link=None,is_admin=False, is_staff=False, password=None, is_active=True,):
        if not username:
            raise ValueError("User Must have an username")
        if not password:
            raise  ValueError("User Must have a Password")
        user = self.model(username=username)
        user.set_password(password)
        user.active = is_active
        
        user.gender = gender
        user.profile_url =profile_url
        user.username = username
        user.reset_link = reset_link
        user.full_name = full_name
        user.phone_number = phone_number
        user.email = email
        user.staff = is_staff
        # user.customer = is_customer 
        user.admin = is_admin
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username,full_name=None,phone_number=None, password=None, profile_url=None):

        user = self.create_user(username, email,full_name=full_name,phone_number=phone_number,profile_url=profile_url, is_staff=True,password=password,is_admin=True)
        return user
    def create_staffuser(self, email, full_name=None, password=None):
        user = self.create_user(email, full_name=full_name, password=password, is_staff=True)
        return user
    
class User(AbstractUser):
    # roles = models.OneToOneField(Role, on_delete=models.CASCADE, null=True)
    username = models.CharField(unique=True, max_length=100)
    
    gender = models.CharField(max_length=6,null=True, blank=True)
    profile_url = models.ImageField(upload_to="users")

    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100,unique=True,null=False)
    created_At = models.DateTimeField(auto_now_add=True)
    
    full_name = models.CharField(max_length=255, blank=True, null=True)
    reset_link = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)
    

    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="user", default=None, null=True, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()
    def __str__(self):
        return self.username
    def get_full_name(self):
        return self.full_name
    def get_short_name(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    # @property
    # def is_customer(self):
    #     return self.customer
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)