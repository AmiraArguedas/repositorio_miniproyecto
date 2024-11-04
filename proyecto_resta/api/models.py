from django.db import models
from django.utils import timezone
from datetime import datetime

class CategoriaMenu(models.Model):
    categoria_creada = models.DateTimeField(auto_now_add=True)
    categoria_actualizada = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
####################################################################################

class Menu(models.Model):
    menu_creado = models.DateTimeField(auto_now_add=True)
    menu_actualizado = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.BooleanField(default=True)
    id_categoria = models.ForeignKey(CategoriaMenu, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

####################################################################################

class HistorialEstados(models.Model):   
    historial_creado = models.DateTimeField(auto_now_add=True)
    historial_actualizado = models.DateTimeField(auto_now=True)
    ESTADO_PREPARACION = 'preparación'
    ESTADO_ENVIADO = 'enviado'
    ESTADO_ENTREGADO = 'entregado'

    ESTADOS_CHOICES = [
        (ESTADO_PREPARACION, 'Preparación'),
        (ESTADO_ENVIADO, 'Enviado'),
        (ESTADO_ENTREGADO, 'Entregado')
    ]

    estado = models.CharField(max_length=20, choices=ESTADOS_CHOICES, default=ESTADO_PREPARACION)
    fecha_cambio = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Historial {self.pk} - Estado {self.estado}"

####################################################################################

class Pedido(models.Model):
    pedido_creado = models.DateTimeField(auto_now_add=True)
    pedido_actualizado = models.DateTimeField(auto_now=True)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    id_estado = models.ForeignKey(HistorialEstados, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido {self.pk} - Fecha {self.fecha_pedido}"

####################################################################################

class Promocion(models.Model):
    promocion_creado = models.DateTimeField(auto_now_add=True)
    promocion_actualizado = models.DateTimeField(auto_now=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    descuento = models.IntegerField()
    fecha_vencimiento = models.DateTimeField()
    id_menu = models.ForeignKey(Menu, on_delete=models.CASCADE) 

    def __str__(self):
        return f"Promoción {self.nombre} - {self.id_menu}"

####################################################################################

class MetodoDePago(models.Model):
    metodo_pago_creado = models.DateTimeField(auto_now_add=True)
    metodo_pago_actualizado = models.DateTimeField(auto_now=True)
    tipo_pago = models.CharField(max_length=50)  
    fecha_compra = models.DateField()
    total_compra = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.tipo_pag

####################################################################################



####################################################################################



####################################################################################



####################################################################################
