from django.shortcuts import render
from chinese.models import Category, Food
# Create your views here.
from .models import Cart
def customer_index(request):
    # category, food 보내줘야 돼 -> category만 보내도 되나??
    category = Category.objects.all()
    context = {
        'category':category
    }
    return render(request, 'customer/index.html', context)

def food_detail(request, pk):
    # object 보내줘야 함
    food = Food.objects.get(pk=pk)
    context = {
        'object':food
    }
    return render(request, 'customer/customer_detail.html', context)

def add_cart(request):
    # Cart food_id에 대응되는 데이터의 수량을 add 하다(하나 올려라)
    food_id= request.GET['food_id']
    food = Food.objects.get(pk=food_id)
    # 이전에 해당 음시에 대한 장바구니 정보가 있으면 get(food=food)
    # 없으면 새로 생성해서 적용
    try:
        cart = Cart.objects.get(food=food)
    except:
        cart = Cart.objects.create(food=food)
    finally:
        pass
    cart.amount+=1
    cart.save()
    context = {
        'object':food
    }
    return render(request, 'customer/customer_detail.html',context )
def remove_cart(request):
    food_id= request.GET['food_id']
    food = Food.objects.get(pk=food_id)
    # cart, created = Cart.objects.get_or_create(food=food)    
    cart, _ = Cart.objects.get_or_create(food=food)    
    cart.amount-=1
    cart.save()
    context = {
        'object':food
    }
    return render(request, 'customer/customer_detail.html',context )