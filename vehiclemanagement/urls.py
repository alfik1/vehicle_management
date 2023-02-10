"""vehiclemanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from vehicle import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.SigninView.as_view(),name="signin"),
    path("register",views.SignupView.as_view(),name="register"),
    path("home",views.IndexView.as_view(),name="home"),
    path("vehicleregistration",views.VehicleRegistrationView.as_view(),name="vehicle-registration"),
    path("home/vehicle/<int:id>/vehicleupdate",views.VehicleUpdateView.as_view(),name="vehicle-update"),
    path("vehicle/<int:id>/delete",views.VehicleDeleteView.as_view(),name="delete"),
    path("logout",views.signout_view,name="signout")
]
