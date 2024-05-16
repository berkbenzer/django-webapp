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
from django.urls import path, re_path
from post.views import home_view, homepage_view, artickle_view, kubernetes_view, index_view,translation_view, verbs_view, jenkins_view, aws_view, terraform_view 


urlpatterns = [

    path('', home_view, name='home_view'),
    path('home/', view=homepage_view, name='homepage_view'),
    path('artikles/', view=artickle_view, name='artickle_view'),
    path('kubernetes/', view=kubernetes_view, name='kubernetes_view'),
    path('translation/', view=translation_view, name='translation_view'),
    path('verbs/', view=verbs_view, name='verbs_view'),
    path('jenkins/',view=jenkins_view , name= 'jenkins_view'),
    path('aws/', view=aws_view , name= 'aws_view'),
    path('terraform/', view=terraform_view , name= 'terraform_view'),
    path('techindex/', view=index_view , name= 'index_view'),

] 