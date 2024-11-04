from rest_framework import generics, status
from .models import CategoriaMenu, Menu, HistorialEstados, Pedido, Promocion, MetodoDePago, MesasEstado
from rest_framework.response import Response
from .serializers import CategoriaMenuSerializer, UserRegisterSerializer, MenuSerializer, HistorialEstadosSerializer, PedidoSerializer, PromocionSerializer, MetodoDePagoSerializer, MesasEstadoSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission


class IsAdministrador(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="Admin").exists()
    
class IsCliente(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name="Cliente").exists() 
    
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny] 

##############################################################################################################################

class CategoriaMenuListCreate(generics.ListCreateAPIView):
    queryset = CategoriaMenu.objects.all()
    serializer_class = CategoriaMenuSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

class CategoriaMenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriaMenu.objects.all()
    serializer_class = CategoriaMenuSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Categoría de menú eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)
    
##############################################################################################################################

class MenuListCreate(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Menú eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)

##############################################################################################################################

class HistorialEstadosListCreate(generics.ListCreateAPIView):
    queryset = HistorialEstados.objects.all()
    serializer_class = HistorialEstadosSerializer

class HistorialEstadosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistorialEstados.objects.all()
    serializer_class = HistorialEstadosSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Historial de estados eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)


##############################################################################################################################

class PedidoListCreate(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

##############################################################################################################################

class PromocionListCreate(generics.ListCreateAPIView):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer

class PromocionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer

##############################################################################################################################

class MetodoDePagoListCreate(generics.ListCreateAPIView):
    queryset = MetodoDePago.objects.all()
    serializer_class = MetodoDePagoSerializer


class MetodoDePagoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetodoDePago.objects.all()
    serializer_class = MetodoDePagoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Método de pago eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)


##############################################################################################################################

class MesasEstadoListCreate(generics.ListCreateAPIView):
    queryset = MesasEstado.objects.all()
    serializer_class = MesasEstadoSerializer

    def create(self, request, *args, **kwargs):

        nombre_estado = request.data.get('nombre_estado')
        if nombre_estado not in ['disponible', 'reservada', 'Disponible', 'Reservada']:
            return Response({'error': "El estado debe ser 'disponible' o 'reservada'"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MesasEstadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MesasEstado.objects.all()
    serializer_class = MesasEstadoSerializer

    def update(self, request, *args, **kwargs):
        # Validación adicional en la actualización
        estado = request.data.get('estado')
        if estado and estado not in ['disponible', 'reservada']:
            return Response({'error': "El estado debe ser 'disponible' o 'reservada'."}, status=status.HTTP_400_BAD_REQUEST)

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Estado de mesa eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)
    
##############################################################################################################################



##############################################################################################################################



##############################################################################################################################



##############################################################################################################################
























