from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', unique=True)
    firstname = models.CharField(max_length=120, default='')
    lastname = models.CharField(max_length=120, default='')
    phonenumber = models.CharField(max_length=20, default='')
    birthday = models.DateField(default=timezone.now)
    organization = models.CharField(max_length=120, default='')
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(default=timezone.now)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return self.firstname + " " + self.lastname
    
    def get_short_name(self):
        return self.firstname

class Types(models.Model):
    name = models.CharField(max_length=120, default='', unique=True)

    def __str__(self):
        return self.name

class Competitions(models.Model):
    name = models.CharField(max_length=120)
    startdate = models.DateField(default=timezone.now)
    enddate = models.DateField(default=timezone.now)
    description = models.TextField(null=True)
    uploadeddate = models.DateField(default=timezone.now)

    organizer = models.ForeignKey(User, related_name='competitions', null=True, on_delete=models.SET_NULL)
    type = models.ManyToManyField(Types, related_name='competitions')

    upvote = models.ManyToManyField(User, related_name='upvotedcompetitions', blank=True)
    downvote = models.ManyToManyField(User, related_name='downvotedcompetitions', blank=True)

    delta = models.IntegerField(default=0)

    file = models.FileField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Comments(models.Model):
    body = models.TextField()
    commenteddate = models.DateField(default=timezone.now)

    competition = models.ForeignKey(Competitions, related_name='comments', on_delete=models.CASCADE)
    commenteduser = models.ForeignKey(User, related_name='comments', null=True, on_delete=models.SET_NULL)

    upvote = models.ManyToManyField(User, related_name='upvotedcomments', blank=True)
    downvote = models.ManyToManyField(User, related_name='downvotedcomments', blank=True)

    delta = models.IntegerField(default=0)

    def __str__(self):
        return self.body
    
class Profiles(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    bio = models.CharField(max_length=100, default='', blank=True)

    registeredcompetitions = models.ManyToManyField(Competitions, related_name='profile', blank=True)
    user = models.ForeignKey(User, related_name='profile', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_full_name() if self.user else "No User"
