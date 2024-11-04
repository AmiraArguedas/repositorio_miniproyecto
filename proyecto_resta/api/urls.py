from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user-register'),
    path('categoriamenu/', views.CategoriaMenuListCreate.as_view(), name='categoriamenu-list'), 
    path('categoriamenu/<int:pk>/', views.CategoriaMenuDetail.as_view(), name='categoriamenu-detail'),
    path('mesas/', views.MenuListCreate.as_view(), name='mesas-list'),
    path('mesas/<int:pk>/', views.MenuDetail.as_view(), name='mesas-detail'),
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








]

