from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    #The Capitalized User is built-in model ,we connect it to user
    user  = models.OneToOneField(User)

    #additional
    #Basicly built-in User model has fields like username,password,email but does not have portfolio or profile picture fields
    #Here we add additional input fields and then we will connect them to User built-in model and at the end it will look as 1 form
    portfolio_site = models.URLField(blank = True)

    profile_pic = models.ImageField(upload_to = 'profile_pics',blank = True)

    #On admin panel user profile info first you will see list of usernames
    #if you set it like return self.user.email you will see emails first as list
    def __str__(self):
        return self.user.username
