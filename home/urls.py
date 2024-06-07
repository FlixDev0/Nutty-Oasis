from django.urls import path
from home import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('Productos/', views.products, name="products"),
    path('Ingresar/', views.login, name="login"),
    path('Registrarse/', views.register, name="register"),
]
