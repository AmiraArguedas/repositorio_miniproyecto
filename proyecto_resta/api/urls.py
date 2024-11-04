from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user-register'),
    path('categoriamenu/', views.CategoriaMenuListCreate.as_view(), name='categoriamenu-list'), 
    path('categoriamenu/<int:pk>/', views.CategoriaMenuDetail.as_view(), name='categoriamenu-detail'),
    path('menu/', views.MenuListCreate.as_view(), name='mesas-list'),
    path('menu/<int:pk>/', views.MenuDetail.as_view(), name='mesas-detail'),
    path('historialestados/', views.HistorialEstadosListCreate.as_view(), name='historialestados-list'), 
    path('historialestados/<int:pk>/', views.HistorialEstadosDetail.as_view(), name='historialestados-detail'),
    path('pedidos/', views.PedidoListCreate.as_view(), name='pedidos-list'), 
    path('pedidos/<int:pk>/', views.PedidoDetail.as_view(), name='pedidos-detail'), 
    path('promociones/', views.PromocionListCreate.as_view(), name='promociones-list'), 
    path('promociones/<int:pk>/', views.PromocionDetail.as_view(), name='promociones-detail'), 
    path('metodosdepago/', views.MetodoDePagoListCreate.as_view(), name='metodosdepago-list'),
    path('metodosdepago/<int:pk>/', views.MetodoDePagoDetail.as_view(), name='metodosdepago-detail'),
    path('estadomesas/', views.MesasEstadoListCreate.as_view(), name='estadomesas-list'),
    path('estadomesas/<int:pk>/', views.MesasEstadoDetail.as_view(), name='estadomesas-detail'),
    path('mesas/', views.MesasListCreate.as_view(), name='mesas-list'),
    path('mesas/<int:pk>/', views.MesasDetail.as_view(), name='mesas-detail'),
    path('comentarios/', views.ComentariosListCreate.as_view(), name='comentarios-list'),
    path('comentarios/<int:pk>/', views.ComentariosDetail.as_view(), name='comentarios-detail'),
    path('notificaciones/', views.NotificacionesListCreate.as_view(), name='notificaciones-list'),
    path('notificaciones/<int:pk>/', views.NotificacionesDetail.as_view(), name='notificaciones-detail'),
    path('reservas/', views.ReservaListCreate.as_view(), name='reserva-list'),
    path('reservas/<int:pk>/', views.ReservaDetail.as_view(), name='reserva-detail'),






]

