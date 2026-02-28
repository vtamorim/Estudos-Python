
from app_cadastro import views
from django.urls import path

urlpatterns = [
   #rota,view, nome
   path('',views.home, name='home'),
   path('usuarios/', views.usuarios,name='cadastrar_usuario') 
]
