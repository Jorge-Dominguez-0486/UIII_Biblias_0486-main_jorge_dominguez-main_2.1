from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_biblias, name='inicio_biblias'),
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),

    # --- AGREGAR ESTAS RUTAS PARA PEDIDOS ---
    path('pedidos/', views.ver_pedidos, name='ver_pedidos'),
    path('pedidos/agregar/', views.agregar_pedido, name='agregar_pedido'),
    path('pedidos/actualizar/<int:id>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('pedidos/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_pedido, name='realizar_actualizacion_pedido'),
    path('pedidos/borrar/<int:id>/', views.borrar_pedido, name='borrar_pedido'),
]