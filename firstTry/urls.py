"""firstTry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from webapp.views import (helloWeb,ApiMoney,ApiPersonalProject
        ,ApiPprojMoney,newUser,newMoney,delMoney,addMoneyPage,postNewMoney)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/', include('firstapp.urls')),

    path('api/money/<str:uID>/',ApiMoney),
    path('api/personalproj/<str:uID>/', ApiPersonalProject),
    path('api/projMoney/<str:uID>/', ApiPprojMoney),
    path('newUser/', newUser),
    path('newMoney/',newMoney),
    
    path('web/<str:userID>/', helloWeb),
    path('api/delMoney/', delMoney),

    path('addMoneyPage', addMoneyPage),
    path('postNewMoney/',postNewMoney)
]
