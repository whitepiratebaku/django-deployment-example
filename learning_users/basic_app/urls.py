from django.conf.urls import url
from basic_app import views

#TEMPLATE URLS

#Not Sure
##<li><a class = 'nav-item nav-link' href="{% url 'basic_app:register' %}">Register</a></li>
#the app_name could be the 'basic_app:register' basic_app in above html line in base.html nav link
app_name = 'basic_app'

urlpatterns = [
    #We get here from main project urls.py  ---url(r'^basic_app/',include('basic_app.urls'))---
    #now here we say if there is r'^register/$' in url then go views.register function, and we will use name on html template tag
    #<li><a class = 'nav-item nav-link' href="{% url 'basic_app:register' %}">Register</a></li>
    #the name='register' are basicly 'basic_app:register' register in above html line in base.html nav link
    #The source of r'^register/$' and r'^user_login/$' is views.py file functions
    url(r'^register/$',views.register,name = 'register'),
    url(r'^user_login/$',views.user_login,name = 'user_login')
]
