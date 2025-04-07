
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.json_data),
    path('htmlpage1/', views.page1,name='htmlpage1'),
    path('htmlpage2/', views.page2,name='htmlpage2'),
    path('htmlpage21/', views.page21,name='htmlpage21'),
    path('productpage/',views.products,name='productpage'),
    path('htmlpage3/',views.page3,name='htmlpage3'),
    path('htmlpage4/', views.page4, name='htmlpage4'),
     path('htmlpage41/', views.page41, name='htmlpage41'),
    path('htmlpage5/', views.page5, name='htmlpage5'),
    path('htmlpage6/', views.page6),
    path('display_item/<int:id>/', views.display_item, name='display_item'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
    path('carthtml/',views.cart,name='carthtml'),
    path('addcarthtml/',views.addcart,name='addcarthtml'),
    
]   
