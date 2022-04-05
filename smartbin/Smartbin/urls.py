"""Smartbin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from SmartbinApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.CommonHome,name='CommonHome'),
    path('AdminHome/',views.AdminHome,name='Admin Home'),
    path('CustomerHome/',views.CustomerHome,name='Customer Home'),
    path('CustomerSignUp/',views.CustomerSignUp,name='CustomerSignUp'),
    path('SignIn/',views.SignIn,name='Sign In'),
    
    
    
    path('AdminAddBin/',views.AdminAddBin,name='AdminAddBin'),
    path('AdminViewCustomers/',views.AdminViewCustomers,name='Admin View Customers'),
    path('AdminAddCategory/',views.AdminAddCategory,name='Admin Add Category'),
    path('AdminAddSubCategory/',views.AdminAddSubCategory,name='AdminAddSubCategory'),
    path('AdminAddEvents/',views.AdminAddEvents,name='AdminAddEvents'),
    path('AdminViewFeedback/',views.AdminViewFeedback,name='Admin View Feedback'),
    path('AdminViewProduct/',views.AdminViewProduct,name='AdminViewProduct'),
    path('AdminUpdateProduct/',views.AdminUpdateProduct,name='AdminUpdateProduct'),
    path('AdminAddProduct/',views.AdminAddProduct,name='AdminAddProduct'),
     path('AdminAddBintoMunicipality/',views.AdminAddBintoMunicipality,name='AdminAddBintoMunicipality'),
       path('AdminViewWaste/',views.AdminViewWaste,name='AdminViewWaste'),
        path('AdminViewMuncipality/',views.AdminViewMuncipality,name='AdminViewMuncipality'),
         path('AdminViewAuthority/',views.AdminViewAuthority,name='AdminViewAuthority'),
    path('subcat/',views.subcat,name='subcat'),
    # path('SellerViewBooking/',views.SellerViewBooking,name='SellerViewBooking'),
    
    
     path('CustomerAddEvents/',views.CustomerAddEvents,name='CustomerAddEvents'),
      path('CustomerAddFood/',views.CustomerAddFood,name='CustomerAddFood'),
    path('CustomerAddFeedback/',views.CustomerAddFeedback,name='CustomerAddFeedback'),
    path('CustomerSearchProduct/',views.CustomerSearchProduct,name='CustomerSearchProduct'),
    path('CustomerViewProCategory/',views.CustomerViewProCategory,name='CustomerViewProCategory'),
    path('CustomerViewProSubCategory/',views.CustomerViewProSubCategory,name='CustomerViewProSubCategory'),
    path('CustomerViewProductDetails/',views.CustomerViewProductDetails,name='CustomerViewProductDetails'),
    path('CustomerOrderProduct/',views.CustomerOrderProduct,name="CustomerOrderProduct"),
    path('CustomerViewCart/',views.CustomerViewCart,name="CustomerViewCart"),
    path('CustomerViewMyBooking/',views.CustomerViewMyBooking,name="CustomerViewMyBooking"),
    path('payment1/',views.payment1,name='payment1'),
    path('payment2/',views.payment2,name='payment2'),
    path('payment3/',views.payment3,name='payment3'),
    path('payment4/',views.payment4,name='payment4'),
    path('payment5/',views.payment5,name='payment5'),


  path('AuthoritySignUp/',views.AuthoritySignUp,name='AuthoritySignUp'),
path('AutorityAddWaste/',views.AutorityAddWaste,name='AutorityAddWaste'),
path('AutorityViewevents/',views.AutorityViewevents,name='AutorityViewevents'),
path('AuthorityViewFood/',views.AuthorityViewFood,name='AuthorityViewFood'),


  path('MuncipalitySignUp/',views.MuncipalitySignUp,name='MuncipalitySignUp'),
  path('MuncipalityViewWaste/',views.MuncipalityViewWaste,name='MuncipalityViewWaste'),
path('MuncipalityViewFood/',views.MuncipalityViewFood,name='MuncipalityViewFood'),
path('MuncipalityViewevents/',views.MuncipalityViewevents,name='MuncipalityViewevents')
]
