"""learning_users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from basic_app import views

urlpatterns = [
    #This is basicly for home page,add leads to views.index for other important things
    url(r'^$',views.index,name='index'),
    #This is for admin panel,built-in
    url(r'^admin/', admin.site.urls),
    #This url links to urls.py file in basic_app ,basicly if url something like
    #wwww.mysite.com/things/basic_app then django will go basic_app urls.py for further leading
    #that r'^basic_app/' is basicly says if url has basic_app/ at end then go 'basic_app.urls'
    url(r'^basic_app/',include('basic_app.urls')),
    url(r'logout/$',views.user_logout,name = 'logout')

]
