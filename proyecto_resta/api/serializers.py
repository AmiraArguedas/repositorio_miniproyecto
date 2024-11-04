from rest_framework import serializers
from django.utils import timezone
from datetime import datetime
import re
from .models import CategoriaMenu, Menu, HistorialEstados, Pedido, Promocion, MetodoDePago, MesasEstado, Mesas, Comentarios, Notificaciones, Reserva
from django.contrib.auth.models import User, Group

class CategoriaMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaMenu
        fields = '__all__'
  
        def validate_nombre(self, value):
            if not value.strip():
                raise serializers.ValidationError("El nombre no puede estar vacío.")
   
            if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', value):
                raise serializers.ValidationError("Este campo solo debe contener letras y espacios.")
            return value
        
        def validate_descripcion(self, value):
            if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', value):
                raise serializers.ValidationError("Este campo solo debe contener letras y espacios.")
            return value
        
###################################################################################################################
        
class UserRegisterSerializer(serializers.ModelSerializer):
    role = serializers.CharField(write_only = True)
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'role')
        
    def create(self, validated_data):
        role = validated_data.pop('role')
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        
        if role: 
            try:
                group = Group.objects.get(name = role)
                user.groups.add(group)
                
            except Group.DoesNotExist:
                raise serializers.ValidationError(f"El role '{role}' no existe")
            
        return user

    
###################################################################################################################
    
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
    def validate_nombre(self, value):
        
        if not value.strip():
            raise serializers.ValidationError("El nombre del menú no puede estar vacío.")
        if len(value) < 3:
            raise serializers.ValidationError("El nombre del menú debe tener al menos 3 caracteres.")
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', value):
            raise serializers.ValidationError("Este campo solo debe contener letras y espacios.")
        return value 
    
    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio del menú debe ser un valor positivo.")
        return value

    def validate_categoria(self, value):
        if not value.strip():
            raise serializers.ValidationError("La categoría no puede estar vacía.")
        return value
    
    def validate_descripcion(self, value):
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', value):
            raise serializers.ValidationError("Este campo solo debe contener letras y espacios.")
        return value
    
################################################################################################################### 
    
class HistorialEstadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEstados
        fields = '__all__'

        def validate_estado(self, value):
            validate_states = ['preparación', 'enviado', 'entregado']
            if value not in validate_states:
                raise serializers.ValidationError("Estado no válido. Opciones: 'preparación', 'enviado', 'entregado'.")
            return value
        
        def cambiar_estado(self, nuevo_estado):
        
            if nuevo_estado not in dict(self.ESTADOS_CHOICES):
                raise ValueError("Estado no válido.")
            self.estado = nuevo_estado
            self.fecha_cambio = timezone.now()
            self.save()
        
###################################################################################################################
  
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.values("El precio debe ser mayor a cero")
        return value
    
################################################################################################################### 
    
class PromocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocion
        fields = '__all__'

    def validate(self, attrs):
        if not (0 <= attrs['descuento'] <= 100):
            raise serializers.ValidationError({"descuento": "El descuento debe estar entre 0 y 100."})
        
        if attrs['fecha_vencimiento'] < timezone.now():
            raise serializers.ValidationError({"fecha_vencimiento": "La fecha de vencimiento no puede ser en el pasado."})

        return attrs
        
###################################################################################################################   

class MetodoDePagoSerializer(serializers.ModelSerializer):
     class Meta:
        model = MetodoDePago
        fields = '__all__'

# validaciones 

        def validate_total_compra(self, value):
            if value <= 0:
                raise serializers.ValidationError("El total de la compra debe ser un número positivo.")
            return value

        def validate(self, attrs):
            if attrs.get('tipo_pago') == "":
                raise serializers.ValidationError({"tipo_pago": "El tipo de pago no puede estar vacío."})
            return attrs
    
################################################################################################################### 
    
class MesasEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesasEstado
        fields = ['id', 'nombre_estado']
    
    def validate_estado(self, value):
        if value not in ['disponible', 'reservada', 'Disponible', 'Reservada']:
            raise serializers.ValidationError("El estado debe ser 'disponible' o 'reservada'.")
        return value
        
###################################################################################################################

class MesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesas
        fields = '__all__'

    def validate_capacidad_mesa(self, value): 
        if value <= 0: raise serializers.ValidationError("La capacidad de la mesa debe ser mayor que cero") 
        return value 
    
    def validate_numero_mesa(self, value): 
        if Mesas.objects.filter(numero_mesa=value).exists(): 
            raise serializers.ValidationError("Ya existe una mesa con este número") 
        return value 
    
    def validate_disponibilidad_mesa(self, value): 
        if value.estado == 'Reservada': 
            raise serializers.ValidationError("No se puede agregar una mesa que esté reservada") 
        return value
    
################################################################################################################### 
    
class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        fields = '__all__'
    
    def validate_comentario(self, value): 
        if not value: raise serializers.ValidationError("El comentario no puede estar vacío") 
        if len(value) > 500: # Limitar longitud del comentario 
            raise serializers.ValidationError("El comentario no puede exceder los 500 caracteres") 
        return value 
    
    def validate_calificacion(self, value): 
        if value is None: raise serializers.ValidationError("La calificación es obligatoria") 
        if value < 1 or value > 5: raise serializers.ValidationError("La calificación debe estar entre 1 y 5") 
        return value 
    
    def validate_id_menu_comentarios(self, value): 
        if not Menu.objects.filter(id=value.id).exists(): 
            raise serializers.ValidationError("El menú especificado no existe") 
        return value
        
###################################################################################################################

class NotificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificaciones
        fields = '__all__'

    def validate_mensaje(self, value): 
        if not value: 
            raise serializers.ValidationError("El mensaje no puede estar vacío.") 
        if len(value) > 500: 
            raise serializers.ValidationError("El mensaje no puede exceder los 500 caracteres") 
        return value 
    
################################################################################################################### 
    
class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

# validaciones 

    def validate(self, attrs):
        if attrs['fecha_reserva'] < timezone.now():
            raise serializers.ValidationError({"fecha_reserva": "La fecha de reserva no puede ser en el pasado."})
        
        if not Mesas.objects.filter(id=attrs['id_mesa'].id).exists():
            raise serializers.ValidationError({"id_mesa": "La mesa especificada no existe."})

        return attrs
        
###################################################################################################################    