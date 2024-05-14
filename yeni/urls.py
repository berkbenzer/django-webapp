"""
URL configuration for yeni project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from post.views import home_view, artickle_view, translation_view, verbs_view, sinarch_view,jenkins_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('artikles.html/', artickle_view, name='artickle_view'),
    path('translation.html/', translation_view, name='translation_view'),
    path('verbs.html/', verbs_view, name='verbs_view'),
    path('singlearch.html/',sinarch_view , name= 'sinarch_view'),
    path('jenkins.html/',jenkins_view , name= 'jenkins_view')

] 