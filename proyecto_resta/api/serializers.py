from rest_framework import serializers
from django.utils import timezone
from datetime import datetime
import re
from .models import CategoriaMenu, Menu, HistorialEstados, Pedido, Promocion
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


    
################################################################################################################### 
    
    
        
###################################################################################################################


    
################################################################################################################### 
    
    
        
###################################################################################################################


    
################################################################################################################### 
    
    
        
###################################################################################################################    