from django.shortcuts import render
from chinese.models import Category, Food
def index(request):
    category = Category.objects.all()
    food = Food.objects.all()
    context = {
        'category':category,
        'food':food
    }
    return render(request, 'index.html', context)