#urls.py
from django.urls import path
from .views import home, login_view, logout_view, register_view, index
from . import views
urlpatterns = [
    path('', home, name='home'), 
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path('register/', register_view, name='register'),
    
    path('', index, name='index'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    
]
