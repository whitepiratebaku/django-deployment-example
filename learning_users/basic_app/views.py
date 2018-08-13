from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    #the 'basic_app/index.html' leads to '\templates\basic_app\index.html'
    return render(request , 'basic_app/index.html')


#this function is for learning purposes.Imagine user needs to be logged in in order to see profile page
#with this @login_required decorator we can set login requirement for function to work
@login_required
def special(request):
    return HttpResponse("You are logged in,Nice!")

#the below decorator is for to make sure that user logged in before logging out user
#If we dont specify it we can get errors
#It is simple logic you need to be logged in in order to log out
@login_required
def user_logout(request):
    #built-in function logsout user
    logout(request)

    #Then we redirect user to home page
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered = False

    #Check if user clicked Register button
    if request.method == "POST":
        #we will use following values in registration.html file as template tags
        #Not sure  ,I think here we get data from user and save it to variable
        #it happens after user click Register button
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        #If all data we get from user is valid then do following
        if user_form.is_valid() and profile_form.is_valid():

            #After check data is valid we save it

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            #Not sure I think somehow we connect form results
            #Not sure but I think this line has some relation with line(I write it down) in models.py under UserProfileInfoForm class
            #user  = models.OneToOneField(User)
            profile.user = user

            #Here we check if picture submited
            if 'profile_pic' in request.FILES:
                #here we assign picture to profile.profile_pic
                #This profile_pic are from models.py ,you can see it there
                #Not Sure:like profile_pic is in models.py  then it connected to forms.py with UserProfileInfoForm
                #then connected to views.py via UserProfileInfoForm
                profile.profile_pic = request.FILES['profile_pic']
            #Here we save profile ,no matter there is pic or not,it is outside of if
            profile.save()

            #We will use this boolen on registration.html file
            #so if user registered we will show 'Thank you for your registration'
            registered = True
        else:
            #here we print validation errors if happens
            print(user_form.errors,profile_form.errors)
    else:
        #This is for fresh page,I mean above code are mostly about what will happen if user clicks 'Register' button
        #But here we just display forms(like inputboxes,browse file and so),This form is organized by forms.py particularly by UserForm and UserProfileInfoForm
        #Basicly first page shows form with below code then user fills info then click button after click above code works
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    #This returns page,'basic_app/registration.html' is location of html
    #{'user_form':user_form,'profile_form':profile_form,'registered':registered} these things are basicly context ,template tags on html will use these values
    #example this {{ user_form.as_p }}  tag in registration.html
    return render(request,'basic_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

#Login
def user_login(request):
    if request.method == 'POST':
        #username below are from login.html username input tag "<input type="text" name="username" placeholder="Enter Username">"
        #for getting data from html we use .get()
        username = request.POST.get('username')
        #the comment above for username are also for same for password
        password = request.POST.get('password')

        #Below is built-in authenticator,we pass username and password from user to below line
        user = authenticate(username=username,password=password)

        #This checks if authentication was successful
        if user:
            #This checks if user is active
            if user.is_active:
                #now here we actually login the user,before this it was authenticated now is logging in
                login(request,user)
                #Here we direct user to home page
                return HttpResponseRedirect(reverse('index'))
            else:
                #If user is not  active we gonna send http response that user is not active,not redirect just response
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse('Invalid login details supplied')

    else:
        #Here is fresh page again above code is mainly about what will happen after user click login button
        #But below code is just returning fresh,empty login form
        return render(request,'basic_app/login.html',{})
