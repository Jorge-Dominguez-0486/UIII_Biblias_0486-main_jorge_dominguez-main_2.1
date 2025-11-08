from django.shortcuts import render, redirect, get_object_or_404
# Importamos AMBOS modelos
from .models import ClienteGlobal, Pedido

def inicio_biblias(request):
    return render(request, 'inicio.html')

# ===================
# VISTAS PARA CLIENTE
# ===================

def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        pais_residencia = request.POST.get('pais_residencia')
        ClienteGlobal.objects.create(
            nombre=nombre, apellido=apellido, email=email, pais_residencia=pais_residencia
        )
        return redirect('ver_clientes')
    return render(request, 'cliente/agregar_cliente.html')

def ver_clientes(request):
    clientes = ClienteGlobal.objects.all()
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

def actualizar_cliente(request, id):
    cliente = get_object_or_404(ClienteGlobal, id=id)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def realizar_actualizacion_cliente(request, id):
    cliente = get_object_or_404(ClienteGlobal, id=id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.email = request.POST.get('email')
        cliente.pais_residencia = request.POST.get('pais_residencia')
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, id):
    cliente = get_object_or_404(ClienteGlobal, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# ===================
# VISTAS PARA PEDIDO
# ===================

def ver_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-fecha_hora')
    return render(request, 'pedido/ver_pedidos.html', {'pedidos': pedidos})

def agregar_pedido(request):
    clientes = ClienteGlobal.objects.all() 
    
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        cliente_obj = get_object_or_404(ClienteGlobal, id=cliente_id)
        
        Pedido.objects.create(
            cliente=cliente_obj,
            total_neto=request.POST.get('total_neto', 0),
            metodo_pago=request.POST.get('metodo_pago'),
            estado_pedido=request.POST.get('estado_pedido', 'Pendiente'),
            impuesto_total=request.POST.get('impuesto_total', 0),
            costo_envio=request.POST.get('costo_envio', 0),
            direccion_envio=request.POST.get('direccion_envio')
        )
        return redirect('ver_pedidos')
    
    return render(request, 'pedido/agregar_pedido.html', {'clientes': clientes})

def actualizar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    clientes = ClienteGlobal.objects.all()
    context = {
        'pedido': pedido,
        'clientes': clientes
    }
    return render(request, 'pedido/actualizar_pedido.html', context)

def realizar_actualizacion_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        pedido.cliente = get_object_or_404(ClienteGlobal, id=cliente_id)
        pedido.total_neto = request.POST.get('total_neto')
        pedido.metodo_pago = request.POST.get('metodo_pago')
        pedido.estado_pedido = request.POST.get('estado_pedido')
        pedido.impuesto_total = request.POST.get('impuesto_total')
        pedido.costo_envio = request.POST.get('costo_envio')
        pedido.direccion_envio = request.POST.get('direccion_envio')
        pedido.save()
        return redirect('ver_pedidos')
    
    clientes = ClienteGlobal.objects.all()
    return render(request, 'pedido/actualizar_pedido.html', {'pedido': pedido, 'clientes': clientes})

def borrar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedidos')
    return render(request, 'pedido/borrar_pedido.html', {'pedido': pedido})