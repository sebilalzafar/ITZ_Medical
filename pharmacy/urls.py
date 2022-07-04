
from django.urls import  path,include
from pharmacy import views

urlpatterns = [
    
    path('pharmacy/',views.pharmacy,name='pharmacy' ),
    path('pharmacy/cart',views.cart,name='cart' ),
]

