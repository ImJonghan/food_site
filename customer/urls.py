from django.urls import path, include
from . import views

app_name = "customer"
urlpatterns = [
    path("", views.customer_index, name='index'),    
    path("food_detail/<int:pk>/", views.food_detail, name='food_detail'),    
    # path("add_cart/", views.add_cart, name='add_cart'), # 장바구니 넣기
    # path("remove_cart/", views.remove_cart, name='remove_cart'), # 장바구니 빼기
    path("modify_cart/", views.modify_cart, name='modify_cart'), 
]
