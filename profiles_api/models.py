from django.db import models

# These are the standard base classes that we need when overriding or customzizing the default django user madel.
# the default django user model.

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""   # define docstring
    # The way User Profiles manager works is the we need to define functions within
    # the manager that can be user to manipulate objects within the modules that manager is for(UserProfile in our case)
    # So, the first function that we need to create is the create underscore use a function.
    def create_user(self, email, name, password=None):  # the user is requiredto have password and won't be able to log in without it.
        """Create a new user profile"""
        if not email:   # if the email passed in is either empty string value or null
            raise ValueError("Users must have an email address")

        #Next, we need normalize the email address so that it makes the second half of the emaill address all lower classes
        email = self.normalize_email(email)

        user.set_password(password)  # this will ensure that the password is converted into a hash
        # next, we create our user model:
        # creates new model that a suer manger is representing.
        user = self.model(email=email, name=name)

        # Next, we need to save the user models
        user.save(using=self._db)  # standard way of savings user such that it supports any database.

        return user # now that we are done creating the user, we need to return the user.


        def create_superuser(self, email, name, password):
            """Create and save a new superuser with given details"""
            user = self.create_user(email, name, password)  # now the we have our super user,

            user.is_superuser = True  # is_superuser is not defined in our UserProfile and that is becuase, PermissionMixin automatically gives us is_superuser
            user.is_staff = AbstractBaseUser
            user.save(using=self._db)

            return user

# Let create a new class called UserpPofile which inherits from the the AbxtractBaseUser and the PermissionMixin base classes
# Here we create UserProfile:  is our database table name, and fields that follows....
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system """       # this doc strings
    # Now, we need to define various fields that we want provide for our user model.
    email = models.EmailField(max_length=255, unique=True)  # This says that we want an "email column" on our User Profile database table which we named it as UserProfile, and we want that column to be an email field, with 255 max characters, and it's unique email. no duplicates.# This tells us that we want an email column in our UserProfile DATABASE table, with max length of 255 and the email is unique
    name =  models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)   # by default, we are saying the user profile to be true.
    is_staff = models.BooleanField(default=False)

    # Next, we need to specify the model manager that we are going to use for our object
    # THis is required because we need to use our custom model for the user model so that it knows how to create, control users.
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'     # Here we are overriding the username filed with our email field, this means the system will require their email insteand of user name and passord to log in.
    REQUIRED_FIELDS = ['name']  # At mininum, we are saying that the user must provide their email address and name

    # GIve django a method to retrieve the full name of the user.
    def get_full_name(self):
        """Retrieve full of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name"""       # THis is docstring for documentation of what we are doing in this method.
        return self.name

    # We need to define a method that will return a sting represtation of the user:
    def __str__(self):
        """String represtentation of our user"""
        return self.email
