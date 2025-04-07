from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Myusers
from project.models import Myusers
from .models import Model1
import json
from django.core.serializers import serialize
#--- when receiving data from another front end 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
#--- when receiving data from another front end 
from django.shortcuts import render, get_object_or_404
from django.shortcuts import get_object_or_404, redirect, render

def json_data(request):
   
    return render(request, 'a1.html')

def page1(request):
    return render(request,"a.html") 
def cart(request):
    return render(request,"cart.html")  
def addcart(request):
    return render(request,"addcart.html")       
def page2(request):
    print(request)
    if request.method == 'POST': 
        email = request.POST.get('email')
        phone = request.POST.get('mobile')
        pwd = request.POST.get('pwd')
        user = Myusers(mail=email, phone=phone, pwd=pwd)
        user.save()
    return render(request,"a2.html")
def page21(request):
    data =Myusers.objects.all()
    return render(request, 'a21.html', {'data': data})  

def page3(request):
    data = Myusers.objects.all()
    return render(request, 'a3.html', {'data': data}) 

def page4(request):
    if request.method == 'POST': 
        name = request.POST.get('name')
        url = request.POST.get('imgurl')
        description = request.POST.get('des')
        price = request.POST.get('price')
        print(name,url,description,price)
        user = Model1(name=name, url=url, description=description,price=price)
        user.save()
    return render(request,'a4.html')

@api_view(['POST']) # use api_view decorator.
def page41(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            phone = data.get('phone')
            pwd = data.get('pwd')

            user = Myusers(mail=email, phone=phone, pwd=pwd)
            user.save()

            return JsonResponse(
                
                status=status.HTTP_201_CREATED
            )
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"error": "Internal Server Error"}, status=500)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
    

def page5(request):
    data = Model1.objects.all()
    return render(request, 'a5.html', {'data': data})  

    return render(request,'a4.html')
def products(request):
    return render(request,"products.html")
def page6(request):
    data = Myusers.objects.all()
    serialized_data = serialize('json', data)
    json_data = json.loads(serialized_data)
    return JsonResponse(json_data, safe=False)
def display_item(request, id):
    item = get_object_or_404(Myusers, pk=id)
    print(item)
    return render(request, 'display.html', {'item': item})

def update_item(request, id):
    item = get_object_or_404(Myusers, pk=id)
    if request.method == "POST":
        item.mail = request.POST.get('email', item.mail)  # Preserve existing value if empty
        item.phone = request.POST.get('phone', item.phone)
        item.pwd = request.POST.get('pwd', item.pwd)
        item.save()

        # Print updated values for debugging
        print("Updated Email:", item.mail)
        print("Updated Phone:", item.phone)
        print("Updated Password:", item.pwd)

        return redirect('display_item', id=item.id)  # Redirect to show updated values
    return render(request, 'display.html', {'item': item}) 
def delete_item(request, id):
    item = get_object_or_404(Myusers, pk=id)
    if request.method == "POST":  # Ensure deletion happens via POST request
        item.delete()

        # Debugging output to confirm deletion
        print(f"Deleted record: {item.mail}")

        return redirect('htmlpage21')  # Redirect to list view after deletion
    return render(request, 'display.html', {'item': item})  # Optional confirmation page