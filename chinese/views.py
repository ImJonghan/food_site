from django.shortcuts import render
from django.http import HttpResponse
from .models import Food, Category
# Create your views here.

def index(request):
    # get(그냥 주소 입력해서 오면) -> 페이지만 보여주고
    # post -> DB에 입력하는 과정을 넣자
    if request.method=='GET':
        return render(request=request, template_name='chinese/index.html')# 그냥 페이지만 보여주면 됨
    
    elif request.method=='POST':
        # Food.objects.create(name='라떼')
        # request.POST['lion_name']
        category = Category.objects.get(name=request.POST['category'])
        food_name = request.POST['lion_name']
        food_price = request.POST['price']
        food_description = request.POST['description']
        food_takeout = request.POST['takeout']

        Food.objects.create(category= category,name=food_name, price =food_price , description=food_description)        
        return render(request=request, template_name='chinese/index.html')# 그냥 페이지만 보여주면 됨
        
   