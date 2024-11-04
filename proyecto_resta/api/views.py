from rest_framework import generics, status
from .models import CategoriaMenu, Menu, HistorialEstados, Pedido, Promocion, MetodoDePago, MesasEstado, Mesas, Comentarios, Notificaciones, Reserva, Factura, DetallePedido
from rest_framework.response import Response
from .serializers import CategoriaMenuSerializer, UserRegisterSerializer, MenuSerializer, HistorialEstadosSerializer, PedidoSerializer, PromocionSerializer, MetodoDePagoSerializer, MesasEstadoSerializer, MesasSerializer, ComentariosSerializer, NotificacionesSerializer, ReservaSerializer, FacturaSerializer, DetallePedidoSerializer
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
    permission_classes = [IsAuthenticated, IsAdministrador | IsCliente]

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Menú eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)

##############################################################################################################################

class HistorialEstadosListCreate(generics.ListCreateAPIView):
    queryset = HistorialEstados.objects.all()
    serializer_class = HistorialEstadosSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

class HistorialEstadosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistorialEstados.objects.all()
    serializer_class = HistorialEstadosSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Historial de estados eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)


##############################################################################################################################

class PedidoListCreate(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated, IsAdministrador | IsCliente]

class PedidoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

##############################################################################################################################

class PromocionListCreate(generics.ListCreateAPIView):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

class PromocionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promocion.objects.all()
    serializer_class = PromocionSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

##############################################################################################################################

class MetodoDePagoListCreate(generics.ListCreateAPIView):
    queryset = MetodoDePago.objects.all()
    serializer_class = MetodoDePagoSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]


class MetodoDePagoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetodoDePago.objects.all()
    serializer_class = MetodoDePagoSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Método de pago eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)


##############################################################################################################################

class MesasEstadoListCreate(generics.ListCreateAPIView):
    queryset = MesasEstado.objects.all()
    serializer_class = MesasEstadoSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

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
    permission_classes = [IsAuthenticated, IsAdministrador]

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

class MesasListCreate(generics.ListCreateAPIView):
    queryset = Mesas.objects.all()
    serializer_class = MesasSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

# Detail
class MesasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mesas.objects.all()
    serializer_class = MesasSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Mesa eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)
   

##############################################################################################################################

class ComentariosListCreate(generics.ListCreateAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer
    permission_classes = [IsAuthenticated, IsAdministrador | IsCliente]

# Detail
class ComentariosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer
    permission_classes = [IsAuthenticated, IsAdministrador | IsCliente]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Comentario eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)
   

##############################################################################################################################

# ListCreate   
class NotificacionesListCreate(generics.ListCreateAPIView):
    queryset = Notificaciones.objects.all()
    serializer_class = NotificacionesSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

# Detail
class NotificacionesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notificaciones.objects.all()
    serializer_class = NotificacionesSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Notificación eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)


##############################################################################################################################

# ListCreate   
class ReservaListCreate(generics.ListCreateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated, IsAdministrador | IsCliente]

# Detail
class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Reserva eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)

##############################################################################################################################

class FacturaListCreate(generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

# Detail
class FacturaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Factura eliminada correctamente.'}, status=status.HTTP_204_NO_CONTENT)

##############################################################################################################################


class DetallePedidoListCreate(generics.ListCreateAPIView):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

# Detail
class DetallePedidoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]
    

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message': 'Detalle de pedido eliminado correctamente.'}, status=status.HTTP_204_NO_CONTENT)

##############################################################################################################################

class PedidoPorUsuario(generics.ListAPIView):
    serializer_class = PedidoSerializer

    def get_queryset(self):
        id_cliente = self.kwargs['id_cliente']
        return Pedido.objects.filter(cliente_fk=id_cliente)

##############################################################################################################################

class ComentarioPorUsuario(generics.ListAPIView):
    serializer_class = ComentariosSerializer

    def get_queryset(self):
        usuario_id = self.kwargs['usuario_id']
        return Comentarios.objects.filter(cliente_fk=usuario_id)














