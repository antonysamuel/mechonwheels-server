from django.urls import path 
from django.conf.urls import url,include
from rest_framework import routers
from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('viewProduct',views.ProductViewSet)
urlpatterns = [
    path('register/',views.RegisterView.as_view()),
    path('login/',views.LoginView.as_view()),
    path('home/',views.HomeView.as_view()),
    path('workshopHome/',views.WorkshopHomeView.as_view()),
    path('search/',views.SearchView.as_view()),
    path('nearby/',views.NearbyWorkshops.as_view()),
    path('bookService/',views.BookServices.as_view()),
    path('fetchWorks/',views.WorkshopWorks.as_view()),
    path('workStatus/',views.ChangeWorkStatus.as_view()),
    path('searchProducts/',views.SearchProducts.as_view()),
    path('addtoCart/',views.AddtoCart.as_view()),
    path('makeOrder/',views.CreateOrder.as_view()),
    path('getCart/',views.CartViewSet.as_view()),
    path('removeCart/',views.RemoveCart.as_view()),
    path('orderCart/',views.OrderProducts.as_view()),
    path('listSellerProd/',views.ListSellerBookings.as_view()),
    path('listmyProd/',views.ListSellerProducts.as_view()),

    url('',include(router.urls))


    
]