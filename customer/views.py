from django.shortcuts import render
from chinese.models import Category, Food
# Create your views here.

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
