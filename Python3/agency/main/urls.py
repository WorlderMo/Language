from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('order/', views.order, name='order'),
    path('registerUserMessage/', views.registerUserMessage,
         name='registerUserMessage'),
    path('user_login/', views.longinVerify, name='user_login'),
    path('orderMessages/',views.orderMessages,name='orderMessages')
]
