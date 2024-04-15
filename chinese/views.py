from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food, Category
from django.core.files.storage import FileSystemStorage
# Create your views here.

# def upload(request):
#     fs=FileSystemStorage()
#     uploaded_file = request.FILES['file']
#     name = fs.save(uploaded_file.name, uploaded_file)
#     url = fs.url(name)
#     return HttpResponse("{}에 저장이 잘 되었습니다.".format(url))

def add_food(request):
    # get(그냥 주소 입력해서 오면) -> 페이지만 보여주고
    # post -> DB에 입력하는 과정을 넣자
    if request.method=='GET':
        return render(request=request, template_name='chinese/add_food.html')# 그냥 페이지만 보여주면 됨
    
    elif request.method=='POST':
        # Food.objects.create(name='라떼')
        # request.POST['lion_name']
        # Category 인스턴스 가져오는 영역
        category = Category.objects.get(name=request.POST['category'])

        # Food 내용을 구성 영역
        food_name = request.POST['lion_name']
        food_price = request.POST['price']
        food_description = request.POST['description']

        # 이미지 저장 및 url 설정 내용
        fs=FileSystemStorage()
        uploaded_file = request.FILES['file']
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)

        Food.objects.create(category= category,name=food_name, price =food_price , description=food_description,image_url=url)        
        return redirect('index')       
   